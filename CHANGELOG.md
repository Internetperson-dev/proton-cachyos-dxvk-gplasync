### Version 10.0-20251126
* Proton (SLR and Native)
   - Updated to the most recent Proton Experimental release `10.0-202511025` (`experimental-bleeding-edge-10.0-275645-20251126-p1c3998-wdefa42-d8d58ad-vcc9e5e` to be exact).
   - Fixed an issue with Resonite caused by the recently imported wine environment changes (https://github.com/CachyOS/proton-cachyos/issues/80)
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None
* Wine (Standalone)
  - None

> [!WARNING]
> This release includes a `x86_64_v4` package. This package is largely untested and experimental.
> It may exhibit issues or completely refuse to work. Use at your own discretion and report issues [here](https://github.com/CachyOS/proton-cachyos/issues/51) only.

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-comp>

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-275645-20251126-p1c3998-wdefa42-d8d58ad-vcc9e5e

---

### Version 10.0-20251120
* Proton (SLR and Native)
   - Updated to the most recent Proton Experimental release `10.0-202511020`.
   - Fixed an issue that could cause Proton to crash when the Unix environment was too large (https://github.com/CachyOS/proton-cachyos/issues/73)
   - Added the commits from upstream wine that fix Genshin Impact and Zenless Zone Zero high CPU usage again. This time Marvel's Rivals should not crash.
   - Added a patch to fix Girls Frontline crashing on startup. Thanks to @NelloKudo.
   - Added a convinience function in Proton that emulates `DXVK/VKD3D_FRAME_RATE`. It reads the value from the removed `DXVK/VKD3D` env variables, and applies it through `DXVK_CONFIG`. This is added as a convenience and I am not certain if it will remain.
   - Added an `umu.exe` shim executable to start appliations with when using `umu-launcher`. It is derived from `steam.exe` but the Steam specific bits have been removed. It should stop Proton, and thus umu, from exiting prematurely in some cases after starting the target application.
   - Updated dxvk-sarek, dxvk-gplasync and nvidia-libs in proton to check if their respective DLLs are available in the release before including them. This allows for selectively disabling them while testing llvm/arm64 builds. Accompaning options have been added in `configure.sh` to exclude them from a build. Our released builds still include them.
   - Imported a few fixes to NTSync from upstream wine.
   - Imported more commits from upstream Wine for `d2d1`, `windowscodecs`, `vccorlib140`.
   - As usual, imported a couple of wayland-related updates from Proton-EM. This time around they should fix some keyboard input issues.
   - Updated `protonfixes` to https://github.com/open-wine-components/umu-protonfixes/tree/2b33f28
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None
* Wine (Standalone)
  - None

> [!WARNING]
> This release includes a `x86_64_v4` package. This package is largely untested and experimental.
> It may exhibit issues or completely refuse to work. Use at your own discretion and report issues [here](https://github.com/CachyOS/proton-cachyos/issues/51) only.

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-comp>

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20251120

---

### Version 10.0-20251107
* Proton (SLR and Native)
   - This is mostly an incremental update to the most recent Proton Experimental release `10.0-20251106b`.
   - Imported more commits from upstream Wine for `d2d1`, `windowscodecs`, `vccorlib140` and `msvcrt`.
   - As usual, imported a couple of wayland-related updates from Proton-EM.
   - Updated `protonfixes` to https://github.com/open-wine-components/umu-protonfixes/tree/5771780
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None
* Wine (Standalone)
  - None

> [!WARNING]
> This release includes a `x86_64_v4` package. This package is largely untested and experimental.
> It may exhibit issues or completely refuse to work. Use at your own discretion and report issues [here](https://github.com/CachyOS/proton-cachyos/issues/51) only.

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-comp>

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20251106b

---

### Version 10.0-20251023
* Proton (SLR and Native)
   - This is mostly an incremental update to the most recent Proton Experimental release.
   - Removed a few more conflicting `staging` patches which have been superseded in upstream Proton/Wine.
   - Removed dualsense related patches which have been superseded in upstream Proton/Wine.
   - Updated `protonfixes` to https://github.com/open-wine-components/umu-protonfixes/tree/c8e88a9
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None
* Wine (Standalone)
  - None

> [!WARNING]
> This release includes a `x86_64_v4` package. This package is largely untested and experimental.
> It may exhibit issues or completely refuse to work. Use at your own discretion and report issues [here](https://github.com/CachyOS/proton-cachyos/issues/51) only.

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-comp>

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20251023

---

### Version 10.0-20251017
* Proton (SLR and Native)
   - Added `libpcap` for the `wpcap` module in Wine.
   - Added another alternative DXVK, `dxvk-gplasync`, at the requests of our friends at Dawn Winery. Enable using `PROTON_DXVK_GPLASYNC=1`.
   - Imported patches to make Blue Protocol: Star Resonance to work. Thanks to Dawn Winery for the many sleepless nights spent on debugging and working out the issue.
   - Imported `windowscodecs` commits from upstream wine. Might help with taking screenshots in some cases.
   - Removed a few conflicting `staging` patches that have been superseded in upstream Wine. This also includes the "Hide wine version from applications" patch, as it shouldn't be needed by anything. If that's not the case, please report it by opening an issue.
   - Updated `protonfixes` to https://github.com/open-wine-components/umu-protonfixes/tree/596f977
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None
* Wine (Standalone)
  - None

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-comp>

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20251017

---

### Version 10.0-20251015
* Proton (SLR and Native)
   - Just a version bump of the base proton bleeding edge version.
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None
* Wine (Standalone)
  - None

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-comp>

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-255917-20251015-p30f753-w92e7a7-ddf74ab-v4ce928

---

### Version 10.0-20251008
* Proton (SLR and Native)
   - Updated DXVK to fix issues with Elite Dangerous.
   - Updated `dxvk` to https://github.com/doitsujin/dxvk/tree/df74ab52
   - Updated `vkd3d-proton` to https://github.com/HansKristian-Work/vkd3d-proton/tree/4ce92864
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None
* Wine (Standalone)
  - None

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-comp>

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20251006b

---

### Version 10.0-20251007
* Proton (SLR and Native)
   - Removed a number of commits that reportedly caused issues with various games, such as Marvel's Rivals. This includes the one helping with Genshin Impact performance.
   - Re-added `DISABLE_LAYER_MESA_ANTI_LAG` when using `PROTON_FSR4_UPGRADE`.
   - Fixed an issue with nvidia-libs handling that resulted in `nvcuda.dll` missing from the prefix. This would cause DLSS Framegen to be unavailable on certain versions of `nvngx_dlssg.dll` shipped with games.
   - Updated `dxvk` to https://github.com/doitsujin/dxvk/tree/55ca713b36f02dcab391df3f847d8713e6150d3e
   - Updated `vkd3d-proton` to https://github.com/HansKristian-Work/vkd3d-proton/tree/abed356c7d6ac592641ed859b9a197b9f00266a0
   - Updated `protonfixes` to https://github.com/open-wine-components/umu-protonfixes/tree/898e3a8d16d180e2ca63ba7a9f750cea1fb45d51
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None
* Wine (Standalone)
  - None

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-compilation

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20251006b

---

### Version 10.0-20251006
* Proton (SLR and Native)
  - Imported a couple of commits from upstream wine to fix Genshin Impact performance. Thanks to @NelloKudo.
  - Imported latest wayland-related commits from Proton-EM. They should fix dead keys when using `winewayland.drv` and DPI scaling. Thanks to @Etaash-mathamsetty.
  - Added an override for umu to use `steam.exe` instead of `start.exe` when launching applications. This is required by certain anime games on Linux. Use `UMU_USE_STEAM=1` to use this alternative path.
  - Updated the default shader cache size for Mesa to 10GB when using `PROTON_LOCAL_SHADER_CACHE=1`.
  - Updated `nvidia-libs/nvcuda` to https://github.com/SveSop/nvcuda/tree/d65952d3814453a91a7e4511ee0fd8203f3a416c
  - Updated `dxvk-sarek` to https://github.com/pythonlover02/DXVK-Sarek/tree/8843c627ffb4a32f184d5ba8100cc31999918a64
  - Updated `protonfixes` to https://github.com/open-wine-components/umu-protonfixes/tree/f7a576d59904936faa39b7ab1c9eb975d04d9aa9
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None
* Wine (Standalone)
  - Imported lsteamclient as a wine module from miniproton. 

> [!WARNING]
> This release includes a `x86_64_v4` package. This package is largely untested and experimental.
> It may exhibit issues or completely refuse to work. Use at your own discretion and report issues [here](https://github.com/CachyOS/proton-cachyos/issues/51) only.

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-compilation

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20251006

---

### Version 10.0-20250919
* Proton (SLR and Native)
  - DXVK is under heavy development at the moment of this release. DXVK and VKD3D-Proton have been updated to the latest version but issues might still arise. Reproduce any issues with Valve's Proton Experimental Bleeding Edge and report them upstream.
  - Updated `PROTON_(DLSS|XESS|FRS4|FSR3)_UPGRADE` cache to hold the compressed archives instead of the extracted DLLs to reduce storage requirements. If you want to remove the old files, delete `~/.cache/protonfixes/upscalers` directory, as they won't be automatically removed.
  - The per-game cache is not enabled by default any more as it seemed to cause confusion. You can enable it using `PROTON_LOCAL_SHADER_CACHE=1` if you want the previous behavior.
  - Removed `GST_GL_WINDOW=surfaceless` when enabling Wayland as it is not as compatible as `x11`. If your game spawns an invisible window on the taskbar under Wayland when playing videos, you can use the previous value to get rid of it.
  - Removed the temporary `DISABLE_LAYER_MESA_ANTI_LAG` flag when using FSR4 upgrade as Anti-Lag 2 should be working properly now. For information on why this was added in the first place refer to https://github.com/CachyOS/proton-cachyos/issues/47.
  - Updated `protonfixes` to https://github.com/Open-Wine-Components/umu-protonfixes/commit/1cec05549e2af5cf454fa748a80b76714ef2e940.
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - This release won't have a native package in CachyOS repositories or the AUR. The reason is that there is too much work-in-progress in DXVK that might cause breakages, and there isn't a user-friendly way to downgrade CachyOS or AUR packages.
  - Despite the above, the source is present in the repository for anyone wanting to build it locally by modifying the existing PKGBUILD, or from my own [repository here](https://github.com/loathingKernel/PKGBUILDs/releases/tag/loathk-public).
  - Removed `piper`, `openfst`, `kaldi` and `vosk` from the build to reduce size and compile time as they were not linking correctly in the native build. They might be included again sometime in the future.
* Wine (Standalone)
  - Removed the "Disable hidraw/Enable SDL" patch as it breaks PlayStation glyphs in games with native DualSense support. You can still disable `hidraw` just like in Proton with `PROTON_DISABLE_HIDRAW=1`. Thanks to @NelloKudo.
  - Imported upstream wine patches to enable `wow64` on multilib builds using `WINEARCH=wow64`. Using `wow64` should fix games that don't play videos due to missing lib32 `ffmpeg` and `gst-plugins` in Arch/CachyOS but also might cause issues with various applications and installers.

> [!WARNING]
> This release includes a `x86_64_v4` package. This package is largely untested and experimental.
> It may exhibit issues or completely refuse to work. Use at your own discretion and report issues [here](https://github.com/CachyOS/proton-cachyos/issues/51) only.

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-compilation

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20250919

---

### Version 10.0-20250906
* Proton (SLR and Native)
  - Fixed `PROTON_(DLSS|XESS|FRS4|FSR3)_UPGRADE` to not download developement versions of upscaler DLLs. This also introduces checksum validation for the cached and installed DLLs.
  - Fixed an issue with windows not focusing properly. This issue made `winecfg` and other similar windows unable to open drop-down menus and focus input fields.
  - Fixed an issue (CachyOS/proton-cachyos#52) with `winewayland.drv` not transitioning from windowed to fullscreen mode properly, with the resulting fullscreen window being offset from the top of the screen in some games. Thanks to @Etaash-mathamsetty.
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - Removed `piper`, `openfst`, `kaldi` and `vosk` from the build to reduce size and compile time as they were not linking correctly in the native build. The might be included again sometime in the future.

> [!WARNING]
> This release includes a `x86_64_v4` package. This package is largely untested and experimental.
> It may exhibit issues or completely refuse to work. Use at your own discretion and report issues [here](https://github.com/CachyOS/proton-cachyos/issues/51) only.

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

> [!NOTE]
> For DXVK-Sarek specific options to tune its behavior refer to: https://github.com/pythonlover02/DXVK-Sarek?tab=readme-ov-file#shader-compilation

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-238230-20250905-p786576-w3f527f-d7cb8e5-v013d33

---

### Version 10.0-20250905
* Proton (SLR and Native)
  - Extended `PROTON_(DLSS|XESS|FRS4|FSR3)_UPGRADE` infrastructure to allow version selection and also cache downloaded DLLs.
    
    | Usage description                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | These options when set to `=1` will work as before, but they will download the latest *available* version, effectively providing automatic updates.                                                                                                                                                                                                                                                                                                           |
    | Furthermore, you can force the the version to download by providing it as the variable's value instead of `1`. For example at the time of writing the latest DLSS version is `310.4.0.0`, if you want to use an earlier version you can do so by setting `PROTON_DLSS_UPGRADE="310.3.0.0"`. You can also write the version partially, and the latest version that matches will be used, i.e. `PROTON_DLSS_UPGRADE="310.2"` will download version `310.2.1.0`. |
    | For FSR4, `PROTON_FSR4_UPRGRADE=1` will download `4.0.2` by default, and `PROTON_FSR4_RDNA3_UPRGRADE=1` will download `4.0.0`. You can override the version in both cases as described above. For example, `PROTON_FSR4_UPRGRADE="4.0.0"` will use `4.0.0` and `PROTON_FSR4_RDNA3_UPRGRADE="4.0.2"` will force `4.0.2` to be used.                                                                                                                            |
    | **Note:** Some DLLs, for example the ones for XeSS and FSR3 do not have consistent versions. In this case the one that matches the specified version will be downloaded and the latest version will be downloaded for the remaining ones.                                                                                                                                                                                                                     |
    | The downloaded DLLs are cached under `~/.cache/protonfixes/upscalers` and depending on options and usage they might require a considerable amount of storage (~500MB).                                                                                                                                                                                                                                                                                        |

  - Increased the per-game shader cache size for Nvidia to 10GiB and added `__GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1` to the effective environment.
  - Imported updates to `amdxc64.dll` from Proton-EM.
  - Added `PROTON_FSR4_INDICATOR` to enable the FSR4 watermark. This doesn't do anything different from `FSR4_WATERMARK` from Proton-EM, it just looked more in-line with the existing options.
  - Updated `nvidia-libs/nvcuda` and `nvidia-libs/nvenc` libraries to the latest version.
  - Re-enabled `asf` plugins for `gst-bad` and `gst-ugly`, might fix some videos not playing.
  - Updated `protonfixes` to https://github.com/Open-Wine-Components/umu-protonfixes/commit/93726321988ac2420ac7535d69972a23f0b2a40a
  - Imported wayland-related commits from upstream wine.
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None

> [!WARNING]
> This release introduces a `x86_64_v4` package. This package is largely untested and experimental. It may exhibit issues and or completely refuse to work. Use at your own discretion and report issues [here](https://github.com/CachyOS/proton-cachyos/issues/51) only.

> [!NOTE]
> For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

> [!NOTE]
> For FSR4 related documentation, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/FSR4.md

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-238230-20250905-p786576-w3f527f-d7cb8e5-v013d33

---

### Version 10.0-20250820
* Proton (SLR and Native)
  - This is a re-relese of **10.0-20250819** with some fixes.
  - Disable AMD Anti-Lag 2 temporarily when `PROTON_FSR4_(RDNA3_)UPGRADE` is used, there are currently issues when both are enabled.
  - Imported wayland-related commits from upstream wine. Might fix The Finals when winewayland is enabled.
  - Imported updates to `amdxc64.dll` from Proton-EM.
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None

**Note:** For wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20250819

---

### Version 10.0-20250819
* Proton (SLR and Native)
  - This is a re-release of `10.0-20250807` re-based on top of `experimental-10.0-20250819` with some additional features and fixes.
  - The `_ntsync` branch has been merged for this release as part of the `main` branch. Disabled by default.
    **Note:** To use NTSync you have to set `PROTON_USE_NTSYNC=1`. Do not trust Mangohud's indicator, it falsely reports that it is using NTSync without this environment variable while in reality it's using FSync/ESync. Verify with `lsof /dev/ntsync`. This is not the same patchset as in Proton-GE/Proton-EM, it's compatibility might differ.

  - Added [dxvk-sarek](https://github.com/pythonlover02/DXVK-Sarek) as an optional DXVK replacement for older GPUs that don't properly support Vulkan 1.3. It is using the `async` branch, so it SHOULD NOT to be used with games using anti-cheat or multiplayer games in general. You have been warned. Use `PROTON_DXVK_SAREK=1` to enable.
  - Fixed an issue with `PROTON_NVIDIA_LIBS` causing games to hang if it was enabled and then disabled.
  - Skip cache cleanup on NVIDIA for per-game shader caches.
  - Allow `DXVK_NVAPI_DRS_SETTINGS` to be overridden by the environment when `PROTON_DLSS_UPGRADE` is used.
  - Changed how upscaler DLL replacement works to allow for multiple of `PROTON_FSR4|FSR3|DLSS|XESS_UPGRADE` to work simultaneously. This is meant to accommodate software such as Optiscaler to find updated DLLs for different upscalers at the same time.
  - Added `PROTON_FSR3_UPGRADE` to upgrade FSR 3.1 DLLs to newer versions.
  - Did the usual video/audio codec whack-a-mole again, some things might work, some things might break. C' est la vie.
  - Added `PROTON_MEDIA_USE_GST` and `PROTON_GST_VIDEO_ORIENTATION` from Proton-GE to support fixes for videos with the wrong orientation.
  - Imported a few upstream commits.
  - Updated `protonfixes` to https://github.com/Open-Wine-Components/umu-protonfixes/commit/a19a272f9df3a56019b8b2914e610de4cc841087
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None

**Note:** For Wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20250819

---

### Version 10.0-20250807
* Proton (SLR and Native)
  - Added downloader for XeSS dlls (version **2.1.0**), similar to the DLSS downloader. Use `PROTON_XESS_UPGRADE=1` environment variable to enable it.
  - Added `PROTON_FSR4_RDNA3_UPGRADE` for RDNA3 GPUs. Does the same thing as `PROTON_FSR4_UPGRADE` but also sets some other necessary variables.
  - Added completer implementations of Nvidia libraries missing from Proton. Should help with enabling options such as PhysX on games they were disabled before. These Nvidia libraries were integrated from https://github.com/SveSop/nvidia-libs. To enable them use `PROTON_NVIDIA_LIBS=1`.  You can also enable them individually using `PROTON_NVIDIA_NVCUDA`, `PROTON_NVIDIA_NVENC`, `PROTON_NVIDIA_NVML` and `PROTON_NVIDIA_NVOPTIX`. These are incompatible with `wow64` and thus disabled when `PROTON_USE_WOW64=1` is set.

    **Important**: If you are using RTX series 4000 or 5000 GPUs you might encounter bad performance or crashes when enabling these with 32bit games. Use`PROTON_NVIDIA_LIBS_NO_32BIT=1` with any of the options above to disable the 32bit and use the 64bit libraries only. Some 32bit games on RTX 4000 and above might still exhibit bad performance with these libraries enabled, e.g. Mirror's Edge.

    **Note**: It is advised that you report issues with these libraries in their respective issue trackers, [nvcuda](https://github.com/SveSop/nvcuda/issues), [nvenc](https://github.com/SveSop/nvenc/issues), [wine-nvml](https://github.com/Saancreed/wine-nvml/issues) and [wine-nvoptix](https://github.com/SveSop/wine-nvoptix/issues). If you don't know what is causing the problem, feel free to open an issue in [proton-cachyos](https://github.com/CachyOS/proton-cachyos/issues) instead.
  - Added per-game shader cache, enabled by default, can be disabled with `PROTON_LOCAL_SHADER_CACHE=0`. Shaders will be cached under `<steamlibrary>/shadercache/<appid>` for each game, similarly to when shader pre-caching is enabled. You will get stuttering as the shader cache for each game is rebuilt but the cached shaders won't be evicted due to limited cache size.
  - Ensured that the codecs in FFmpeg match what Valve has enabled in theirs. We still enable more but now we should not miss any by chance.
  - Disabled `codecalpha` from gst-bad which was causing issues with some games with WebM videos when Wine is built with FFmpeg, and re-enabled `winedmo`.
  - Imported wayland related commits from Proton-EM ([up to EM-10.0-2B](https://github.com/Etaash-mathamsetty/Proton/tree/EM-10.0-2B)).
  - Imported a few upstream commits.
  - Fix `protonfixes` not de-symlinking prefix files properly. Should fix issues with installing some winetricks verbs.
  - Updated protonfixes to https://github.com/Open-Wine-Components/umu-protonfixes/commit/5cdfd3608d513bc9ff9c2d1a642ebd85687fbc1e
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None

**Note:** There is a testing version with NTSync available here:
* https://share.cachyos.org/proton/proton-cachyos-10.0-20250807-slr-ntsync-x86_64.tar.xz
* https://share.cachyos.org/proton/proton-cachyos-10.0-20250807-slr-ntsync-x86_64_v3.tar.xz

To use NTSync you have to set `PROTON_USE_NTSYNC=1`. Do not trust `mangohud`'s indicator, it falsely reports that it is using NTSync without this
environment variable while in reality it's using FSync/ESync. Verify with `lsof /dev/ntsync`. We want to be certain it doesn't cause regressions
hence we are not including it with in the main packages. This is not the same patchset as in Proton-GE/Proton-EM, it's compatibility might differ.

**Note:** For wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-228005-20250807-p29548f-w253fb0-d835e98c-vb72e62

---

### Version 10.0-20250714
* Proton (SLR and Native)
  - Added downloader for DLSS dlls (version **310.3.0**), similar to the FSR4 downloader. Use `PROTON_DLSS_UPGRADE=1` environment variable to enable it.
  - Added `PROTON_DLSS_INDICATOR=1` environment variable to enable DLSS hud.
  - Reverted `PROTON_FSR4_UPGRADE=1` downloader to install version **4.0.0** of `amdxcffx64.dll`.
  - Imported wayland related commits from Proton-EM.
  - Updated protonfixes to https://github.com/Open-Wine-Components/umu-protonfixes/commit/cf8d5a2ef83d09f84ba4fa475b01b889d97f6300
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None

**Note:** There is a testing version with NTSync available here: https://share.cachyos.org/proton/proton-cachyos-10.0-20250714-ntsync-slr.tar.xz
To use NTSync you have to set `PROTON_USE_NTSYNC=1`. Do not trust `mangohud`'s indicator, it falsely reports that it is using NTSync without this environment variable while in reality it's using FSync/ESync. Verify with `lsof /dev/ntsync`. We want to be certain it doesn't cause regressions hence we are not including it with in the main packages. This is not the same patch-set as in Proton-GE/Proton-EM, it's compatibility might differ.

For wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-220315-20250715-pe2a550-wef1fe3-d614d6a-v6f32f6

---

### Version 10.0-20250702
* Proton (SLR and Native)
  - Imported upstream wine commits for wayland.
  - Added a missing patch for Vanguard: Saga of Heroes.
  - Updated `amdxcffx64.dll` downloader to install version `4.0.1`.
  - Added patches for AMD's Anti Lag 2 for `vkd3d-proton` and `wine`. Requires patched `Mesa`.
  - Added `PROTON_ENABLE_MEDIACONV` env variable to enable proton mediaconverter. Mostly for testing purposes.
  - Updated protonfixes to https://github.com/Open-Wine-Components/umu-protonfixes/commit/4d51fad0b5f897a87d46cf69a8bf53fa0a0df48b
  - Added patch for protonfixes to use `vcrun2022` instead of `vcrun2019`. Fixes winetricks forcing Windows 7 as the version of the prefix.
* Proton (SLR specific)
  - Revert to `-O2` (the default) instead of `-O3`. It wasn't an issue for the SLR build but prefer to have less variance between builds.
* Proton (Native specific)
  - None

For wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-215098-20250702-pefce1a-wf6650a-deb0d67-v3a3642

---

### Version 10.0-20250623
* Proton (SLR and Native)
  - Imported wayland specific patches from Proton-EM. Thanks to [Etaash-mathamsetty](https://github.com/Etaash-mathamsetty).
  - Imported upstream patches for d2d1 since wine-10.0. Fixes "Sickly Days and Summer Traces". Thanks to [R1kaB3rN](https://github.com/R1kaB3rN).
  - Imported more upstream commits relating to wayland.
  - Added patches to help with better anticheat integration. Thanks to [NelloKudo](https://github.com/NelloKudo/) et al.
  - Added automatic download for `amdxcffx64.dll` using `PROTON_FSR4_UPGRADE`.
  - Disabled winedmo (ffmpeg) for Wine. Fixes crash in Devil May Cry HD Collection.
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None

For wayland specific flags and options, please refer to: https://github.com/Etaash-mathamsetty/Proton/blob/em-10/docs/EM-ADDITIONS.md

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-211434-20250623-p534f89-w293d64-de4989d-v59e50c

---

### Version 10.0-20250605
* Proton (SLR and Native)
  - Disable proton media converter by default in Wine. We ship more than enough codecs to not need it. This affects standalone Wine mostly, since in Proton it was already being disabled through the related environment variables.
  - Set `GST_GL_WINDOW` to `surfaceless` instead of `x11` in Wine. Again, mostly affects standalone Wine.
  - Update wayland specific patches.
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - None

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-206012-20250606-pc3a07e-wac8f23-d09e4bc-v4a0688

---

### Version 10.0-20250601
* Proton (SLR and Native)
  - FFmpeg has been bumped from `6.1.2` to `7.1.1`
  - Every decoder, demuxer, parser, filter has been enabled in FFmpeg
  - GStreamer and gst-plugins have been bumped to `1.26.1`
  - Updated protonfixes to https://github.com/Open-Wine-Components/umu-protonfixes/commit/50a611291caf0527b89dc55602afe66070d6c544
  - Imported new Wayland related patches from [Proton-EM-10.0-19](https://github.com/Etaash-mathamsetty/Proton/releases/tag/EM-10.0-19)
  - Ignore steam input virtual controller when PROTON_PREFER_SDL is set (thanks to [Etaash-mathamsetty](https://github.com/Etaash-mathamsetty))
* Proton (SLR specific)
  - None
* Proton (Native specific)
  - Build openfst,kaldi,vosk,piper for native version again (they are still not found while building, so no support in wine yet)
  - Clean up Steam's default Scout environment when using the native version of `proton-cachyos`

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-204012-20250601-pdce981-w6a4d0d-d4f47cb-vf96654

---

### Version 10.0-20250520
* Proton
  - Enable application-specific workarounds when using the Wayland driver by default
  - Remove media converter from `winedmo` and reenable FFmpeg for Wine, bump it to 6.1.2.
  - Import patches from Proton-EM to disable mouse acceleration, enable touchpad scrolling, and handling of rotated screens.
  - Revert to using Valve's Sniper SDK since we do not need to build `python-xlib` presently, and for transparency.

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-199576-20250520-p6aacad-w900d43-d61b91e-v7e829e

---

### Version 10.0-20250515
* Proton
  - HDR is NOT enabled by default with Wayland any more, use `PROTON_ENABLE_HDR=1` to enable when enabling Wayland.
  - Added wayland-specific command line arguments for various launchers under wayland. Thanks [Etaash-mathamsetty](https://github.com/Etaash-mathamsetty)
  - Added patches to use system cursor shapes when possible. MR: https://gitlab.winehq.org/wine/wine/-/merge_requests/7678
  - Fix issue with libvkd3d related crashes in UnderRail.
  - Fix issue with libvkd3d missing from the default prefix in the native version.
  - Fix issue with libxkbcommon trying to install bash completion related files to the host while building.
  - Use UMU SDK to build the Steam Linux Runtime version

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-bleeding-edge-10.0-198042-20250515-pba2272-w88783e-de9eff9-vb57878

---

### Version 10.0-20250509
* Proton
  - Rebased almost all patches from **Proton Cachyos 9.0**.
  - Enabled the Wayland driver for the Steam Linux Runtime builds too. Enable with `PROTON_ENABLE_WAYLAND=1`. Thanks to [GloriousEggroll](https://github.com/GloriousEggroll) for making it happen.
  - Added a lot of Wayland related patches from upstream wine that happened after the release of wine-10.0
  - Fixed various issues with the Wayland driver and Vulkan games. Thanks to [Etaash-mathamsetty](https://github.com/Etaash-mathamsetty) for all the hard work.
  - Added a stub implementation for `amdxc64.dll` to enable FSR4. Use `FSR4_UPGRADE=1` to upgrade FSR3.1 games to FSR4. Again thanks to [Etaash-mathamsetty](https://github.com/Etaash-mathamsetty). Instructions: https://github.com/Etaash-mathamsetty/wine-builds/releases/tag/fsr4
  - Added DualSense related patches for more complete audio device detection functionality for wired sound-based haptics. Some games that relied on that specific behaviour should now have that functional. Thanks to [ClearlyClaire](https://github.com/ClearlyClaire) for the original patches and [Exotic0015](https://github.com/Exotic0015) for looking into it since **Proton Cachyos 9.0**. Upstream: https://gitlab.winehq.org/wine/wine/-/merge_requests/7238
  - Removed the Dragon Age Inquisition patch as it was not working. Please use **Proton-Cachyos 9.0** for now with that game.
  - Updated the NTSync branch to Proton 10.0. Thanks to [whrvt](https://github.com/whrvt). No, NTSync is not merged into Proton-CachyOS yet, sorry.

  - Thanks to everyone on the CachyOS Discord server who provided testing while working on this. And special thanks to the people mentioned above and [NelloKudo](https://github.com/NelloKudo/) for sharing the workload.

**Base:** https://github.com/ValveSoftware/Proton/tree/experimental-10.0-20250509

---
