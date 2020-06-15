## Example of Godot Foreigner (FFI library) project & export setup

[Foreigner](https://github.com/and3rson/foreigner) is a *Foreign
Function Interface* (FFI) addon/plugin for the [Godot game
engine](https://godotengine.org/). It wraps the [`libffi` FFI
library](http://sourceware.org/libffi/) and makes the functionality
available to applications built with Godot.

This repository contains an example of how to set up a project to use
Foreigner and successfully export applications (along with their
supporting dynamic/shared libraries) to run on three different
platforms (without additional compilation steps--assuming the shared
libraries you're using are supplied as binaries):

 * Linux

 * Mac

 * Win64

### How to use

Open/import the example project via the Godot Project Manager or
export binaries via the Godot command line feature.

### Licenses

 * License for items specific/unique to this example:

    * MIT: See [`LICENSE`](LICENSE)

 * License for bundled Foreigner library binaries (currently based on
   [this branch](https://github.com/follower/foreigner/tree/add-build-win64-on-linux-cross-compile-support)):

    * MIT: See [`licenses/LICENSE.foreigner`](licenses/LICENSE.foreigner)

 * License for statically linked `libffi`:

    * See: [`licenses/LICENSE.libffi`](licenses/LICENSE.libffi)

The statically linked Foreigner shared library binaries may also
contain items covered by other licenses, see the source and/or build
configuration for details.
