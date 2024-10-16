// import TextField from "@mui/material/TextField";
// import Button from "@mui/material/Button";
// import FormControlLabel from "@mui/material/FormControlLabel";
// import Checkbox from "@mui/material/Checkbox";
// import Container from "@mui/material/Container";
// import Grid from "@mui/material/Grid2";
// import Typography from "@mui/material/Typography";
import {
  TextField,
  Button,
  FormControlLabel,
  Checkbox,
  Grid2,
  Link,
  Typography,
  Container,
} from "@mui/material";

function SginIn() {
  return (
    <Container maxWidth="xs">
      <Typography
        component="h1"
        variant="h4"
        sx={{
          width: "100%",
          fontSize: "clamp(2rem, 10vw, 2.15rem)",
          mb: 2,
          mt: 8,
        }}
      >
        Sign in
      </Typography>
      <TextField
        label="Email Address"
        required
        fullWidth
        name="email"
        autoFocus
      />
      <br />
      <TextField
        label="Password"
        type="password"
        required
        fullWidth
        name="password"
      />
      <FormControlLabel
        control={<Checkbox value="remember" color="primary" />}
        label="Remember me"
      />
      <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
        Sign in
      </Button>
      <Grid2 container spacing={2}>
        <Grid2 size="grow">
          <Link href="../forgotpwd">Forgot Passowrd?</Link>
        </Grid2>
        <Grid2 item>
          <Link href="../signup">Sign Up</Link>
        </Grid2>
      </Grid2>
    </Container>
  );
}

export default SginIn;
