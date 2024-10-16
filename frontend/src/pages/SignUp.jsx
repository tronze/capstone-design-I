import {
  Typography,
  Button,
  Checkbox,
  FormControlLabel,
  Link,
  TextField,
  Container,
  Stack,
} from "@mui/material";

const SignUp = () => {
  return (
    <div>
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
          Sign up
        </Typography>
        <Stack spacing={2}>
          <TextField
            label="성"
            name="secondName"
            required
            fullWidth
            autoFocus
            placeholder="Hong"
          />
          <TextField
            label="이름"
            name="firstNmae"
            required
            fullWidth
            placeholder="Gildong"
          />
          <TextField
            label="Email"
            name="email"
            required
            fullWidth
            placeholder="scholpion@email.com"
            variant="outlined"
          />
          <TextField
            label="PassWord"
            required
            fullWidth
            name="password"
            placeholder="••••••"
            type="password"
            variant="outlined"
          />
        </Stack>
        <FormControlLabel
          control={<Checkbox value="allow" color="primary" />}
          label="페이지 정책에 동의합니다"
        />
        <Button type="submit" fullWidth variant="contained" sx={{ mt: 2 }}>
          Sign up
        </Button>
        <Typography sx={{ textAlign: "center", mt: 2 }}>
          Already have an account?{" "}
          <span>
            <Link
              href="../signin/"
              variant="body2"
              sx={{ alignSelf: "center" }}
            >
              Sign in
            </Link>
          </span>
        </Typography>
      </Container>
    </div>
  );
};

export default SignUp;
