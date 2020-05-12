{ p ? import (fetchTarball https://github.com/NixOS/nixpkgs-channels/archive/nixos-unstable.tar.gz) {} }:

p.mkShell {
  buildInputs = [
    p.drawpile
    p.mumble
  ];
}
