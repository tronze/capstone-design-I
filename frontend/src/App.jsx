import SignIn from "./pages/SignIn";
import { Routes, Route } from "react-router-dom";
import SignUp from "./pages/SignUp";
import Home from "./pages/Home";
import ForgotPwd from "./pages/ForgotPwd";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/forgotpwd" element={<ForgotPwd />} />
      </Routes>
    </>
  );
}

export default App;
