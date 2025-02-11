const passport = require("passport");
const SamlStrategy = require("passport-saml").Strategy;

const samlConfig = {
  entryPoint: process.env.SAML_ENTRY_POINT,
  issuer: process.env.SAML_ISSUER,
  callbackUrl: process.env.SAML_CALLBACK_URL,
  cert: process.env.SAML_CERT, // SAML provider certificate
};

passport.use(
  new SamlStrategy(samlConfig, (profile, done) => {
    return done(null, {
      id: profile.nameID,
      email: profile.email,
    });
  })
);

module.exports = passport;
