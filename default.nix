with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "losp.us";
  buildInputs = [jekyll];
  src = lib.cleanSource ./.;
  buildPhase = ''
    jekyll build
  '';
  installPhase = ''
    mv _site $out
  '';
}
