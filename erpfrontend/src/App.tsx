import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import ProtectedRoute from "./components/ProtectedRoute";
import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";
import { ROLES } from "./types/auth";

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          {/* Public routes */}
          <Route path="/login" element={<LoginPage />} />

          {/* Protected – RH + ADMIN can access everything below */}
          <Route element={<ProtectedRoute allowedRoles={[ROLES.ADMIN, ROLES.RH]} />}>
            <Route path="/"           element={<DashboardPage />} />
            <Route path="/employes"   element={<DashboardPage />} />
            <Route path="/departements" element={<DashboardPage />} />
            <Route path="/conges"     element={<DashboardPage />} />
            <Route path="/absences"   element={<DashboardPage />} />
            <Route path="/paie"       element={<DashboardPage />} />
            <Route path="/parametres" element={<DashboardPage />} />
          </Route>

          {/* Protected – ADMIN only */}
          <Route element={<ProtectedRoute allowedRoles={[ROLES.ADMIN]} />}>
            <Route path="/admin/keycloak" element={<DashboardPage />} />
          </Route>

          {/* Fallback */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;

