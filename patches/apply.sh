#!/usr/bin/env bash
set -eu

patch_cmd() {
    echo "Applying:: $(basename "$1")"
    patch -Np1 -i "$1"
}

here="$(dirname "$(realpath "$0")")"

pushd "$here"/../gstreamer || exit 1
    patch_cmd "$here"/gstreamer/gstreamer-5509.patch
    patch_cmd "$here"/gstreamer/gstreamer-5511.patch
popd || exit 1

pushd "$here"/../openfst || exit 1
    patch_cmd "$here"/openfst/openfst-879f09d2ac799cca99b78de3442194ebbe29d24a.patch
    patch_cmd "$here"/openfst/openfst-18e94e63870ebcf79ebb42b7035cd3cb626ec090.patch
popd || exit 1

pushd "$here"/../protonfixes || exit 1
    patch_cmd "$here"/protonfixes/protonfixes-0001-Makefile-skip-python-xlib.patch
popd || exit 1

pushd "$here"/../glslang || exit 1
    patch_cmd "$here"/glslang/glslang-renderdoc-1.36-gcc15-fix.patch
popd || exit 1

pushd "$here"/../vkd3d-proton || exit 1
    patch_cmd "$here"/vkd3d-proton/vkd3d-proton-0001-vkd3d-Load-amdxc64-when-using-AMD.patch
popd || exit 1
