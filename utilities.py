"""Various utility functions for use in the proton script"""

import sys
import os
from argparse import Namespace
from pathlib import Path

base_config = Path(os.getenv('XDG_CONFIG_HOME', '~/.config')).expanduser()
base_cache = Path(os.getenv('XDG_CACHE_HOME', '~/.cache')).expanduser()


class Config(Namespace):
    class Path(Namespace):
        config_dir: Path = base_cache.joinpath('protonfixes')
        cache_dir: Path = base_cache.joinpath('protonfixes')

    path = Path()


class Log:
    @staticmethod
    def info(msg):
        sys.stderr.write('[Utilities] INFO: ' + msg)
        sys.stderr.flush()

    @staticmethod
    def warn(msg):
        sys.stderr.write('[Utilities] WARN: ' + msg)
        sys.stderr.flush()

    @staticmethod
    def crit(msg):
        sys.stderr.write('[Utilities] ERROR: ' + msg)
        sys.stderr.flush()


config = Config()
log = Log()


def primary_gpu_supports_vulkan(major: int, minor: int, patch: int = 0, /, device_filter: str = '') -> bool:
    from ctypes import cast, POINTER, c_char_p, c_uint32, c_void_p

    from vulkan import (vkCreateInstance, vkDestroyInstance, VkInstanceCreateInfo, VkStructureType, VkApplicationInfo,
                        vkEnumeratePhysicalDevices, VkPhysicalDeviceProperties2, vkGetPhysicalDeviceProperties2,
                        VK_MAKE_VERSION, VkPhysicalDeviceType)

    vk_instance = c_void_p(0)

    create_instance_result = vkCreateInstance(VkInstanceCreateInfo(
        sType=VkStructureType.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO.value,
        pNext=0,
        flags=0,
        pApplicationInfo=cast(0, POINTER(VkApplicationInfo)),
        enabledLayerCount=0,
        ppEnabledLayerNames=cast(0, POINTER(c_char_p)),
        enabledExtensionCount=0,
        ppEnabledExtensionNames=cast(0, POINTER(c_char_p))
    ), c_void_p(0), vk_instance)
    if create_instance_result != 0:
        # FIXME: What do we do in a failure case?
        return True

    num_devices = c_uint32(0)
    num_devices_result = vkEnumeratePhysicalDevices(vk_instance, num_devices, cast(0, POINTER(c_void_p)))
    if num_devices_result != 0:
        return True

    devices = (c_void_p * num_devices.value)(0)
    devices_handle_result = vkEnumeratePhysicalDevices(vk_instance, num_devices, cast(devices, POINTER(c_void_p)))
    if devices_handle_result != 0:
        return True

    properties2 = VkPhysicalDeviceProperties2()
    version_to_check = VK_MAKE_VERSION(major, minor, patch)
    # True/False -> supported/not supported, -1 -> device type not present
    discrete_gpu_supported = -1
    integrated_gpu_supported = -1
    virtual_gpu_supported = -1
    for device in devices:
        # FIXME: Can this fail?
        vkGetPhysicalDeviceProperties2(device, properties2)

        if device_filter not in properties2.properties.deviceName.decode():
            continue

        device_type = properties2.properties.deviceType
        supports_requested_version = properties2.properties.apiVersion >= version_to_check

        if discrete_gpu_supported != True and device_type == VkPhysicalDeviceType.VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU.value:
            discrete_gpu_supported = supports_requested_version
        if integrated_gpu_supported != True and device_type == VkPhysicalDeviceType.VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU.value:
            integrated_gpu_supported = supports_requested_version
        if virtual_gpu_supported != True and device_type == VkPhysicalDeviceType.VK_PHYSICAL_DEVICE_TYPE_VIRTUAL_GPU.value:
            virtual_gpu_supported = supports_requested_version

    vkDestroyInstance(vk_instance, c_void_p(0))

    if discrete_gpu_supported != -1:
        return discrete_gpu_supported
    if integrated_gpu_supported != -1:
        return integrated_gpu_supported
    if virtual_gpu_supported != -1:
        return virtual_gpu_supported

    return False


if __name__ == '__main__':
    pass


__all__ = ['primary_gpu_supports_vulkan']
