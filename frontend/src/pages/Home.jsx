import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";
const Home = () => {
  const nav = useNavigate();
  return (
    <div>
      <Button onClick={() => nav("./../signin")}>Sign In</Button>
      <Button onClick={() => nav("./../signup")}>Sign Up</Button>
    </div>
  );
};

export default Home;
