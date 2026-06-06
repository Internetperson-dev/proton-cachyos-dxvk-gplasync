from ctypes import (CDLL, c_int, c_void_p, c_uint32, c_char_p, POINTER, Structure, c_float, c_char, c_uint8, c_size_t,
                    c_uint64, c_int32)
from enum import Enum

libvulkan = CDLL('libvulkan.so.1')


# https://docs.vulkan.org/refpages/latest/refpages/source/VkBool32.html
VkBool32 = c_uint32

# https://docs.vulkan.org/refpages/latest/refpages/source/VkDeviceSize.html
VkDeviceSize = c_uint64

# https://docs.vulkan.org/refpages/latest/refpages/source/VkFlags.html
VkFlags = c_uint32

# https://docs.vulkan.org/refpages/latest/refpages/source/VkSampleCountFlags.html
VkSampleCountFlags = VkFlags

# https://docs.vulkan.org/refpages/latest/refpages/source/VkStructureType.html
class VkStructureType(Enum):
    VK_STRUCTURE_TYPE_APPLICATION_INFO = 0
    VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO = 1


# https://docs.vulkan.org/refpages/latest/refpages/source/VkPhysicalDeviceType.html
class VkPhysicalDeviceType(Enum):
    VK_PHYSICAL_DEVICE_TYPE_OTHER = 0
    VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU = 1
    VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU = 2
    VK_PHYSICAL_DEVICE_TYPE_VIRTUAL_GPU = 3
    VK_PHYSICAL_DEVICE_TYPE_CPU = 4


# https://docs.vulkan.org/refpages/latest/refpages/source/VkApplicationInfo.html
class VkApplicationInfo(Structure):
    _fields_ = [
        ('sType', c_int),
        ('pNext', c_void_p),
        ('pApplicationName', c_char_p),
        ('applicationVersion', c_uint32),
        ('pEngineName', c_char_p),
        ('engineVersion', c_uint32),
        ('apiVersion', c_uint32)
    ]


# https://docs.vulkan.org/refpages/latest/refpages/source/VkInstanceCreateInfo.html
class VkInstanceCreateInfo(Structure):
    _fields_ = [
        ('sType', c_int),
        ('pNext', c_void_p),
        ('flags', c_uint32),
        ('pApplicationInfo', POINTER(VkApplicationInfo)),
        ('enabledLayerCount', c_uint32),
        ('ppEnabledLayerNames', POINTER(c_char_p)),
        ('enabledExtensionCount', c_uint32),
        ('ppEnabledExtensionNames', POINTER(c_char_p))
    ]


# https://docs.vulkan.org/spec/latest/chapters/limits.html#VkPhysicalDeviceLimits
class VkPhysicalDeviceLimits(Structure):
    _fields_ = [
        ('maxImageDimension1D', c_uint32),
        ('maxImageDimension2D', c_uint32),
        ('maxImageDimension3D', c_uint32),
        ('maxImageDimensionCube', c_uint32),
        ('maxImageArrayLayers', c_uint32),
        ('maxTexelBufferElements', c_uint32),
        ('maxUniformBufferRange', c_uint32),
        ('maxStorageBufferRange', c_uint32),
        ('maxPushConstantsSize', c_uint32),
        ('maxMemoryAllocationCount', c_uint32),
        ('maxSamplerAllocationCount', c_uint32),
        ('bufferImageGranularity', VkDeviceSize),
        ('sparseAddressSpaceSize', VkDeviceSize),
        ('maxBoundDescriptorSets', c_uint32),
        ('maxPerStageDescriptorSamplers', c_uint32),
        ('maxPerStageDescriptorUniformBuffers', c_uint32),
        ('maxPerStageDescriptorStorageBuffers', c_uint32),
        ('maxPerStageDescriptorSampledImages', c_uint32),
        ('maxPerStageDescriptorStorageImages', c_uint32),
        ('maxPerStageDescriptorInputAttachments', c_uint32),
        ('maxPerStageResources', c_uint32),
        ('maxDescriptorSetSamplers', c_uint32),
        ('maxDescriptorSetUniformBuffers', c_uint32),
        ('maxDescriptorSetUniformBuffersDynamic', c_uint32),
        ('maxDescriptorSetStorageBuffers', c_uint32),
        ('maxDescriptorSetStorageBuffersDynamic', c_uint32),
        ('maxDescriptorSetSampledImages', c_uint32),
        ('maxDescriptorSetStorageImages', c_uint32),
        ('maxDescriptorSetInputAttachments', c_uint32),
        ('maxVertexInputAttributes', c_uint32),
        ('maxVertexInputBindings', c_uint32),
        ('maxVertexInputAttributeOffset', c_uint32),
        ('maxVertexInputBindingStride', c_uint32),
        ('maxVertexOutputComponents', c_uint32),
        ('maxTessellationGenerationLevel', c_uint32),
        ('maxTessellationPatchSize', c_uint32),
        ('maxTessellationControlPerVertexInputComponents', c_uint32),
        ('maxTessellationControlPerVertexOutputComponents', c_uint32),
        ('maxTessellationControlPerPatchOutputComponents', c_uint32),
        ('maxTessellationControlTotalOutputComponents', c_uint32),
        ('maxTessellationEvaluationInputComponents', c_uint32),
        ('maxTessellationEvaluationOutputComponents', c_uint32),
        ('maxGeometryShaderInvocations', c_uint32),
        ('maxGeometryInputComponents', c_uint32),
        ('maxGeometryOutputComponents', c_uint32),
        ('maxGeometryOutputVertices', c_uint32),
        ('maxGeometryTotalOutputComponents', c_uint32),
        ('maxFragmentInputComponents', c_uint32),
        ('maxFragmentOutputAttachments', c_uint32),
        ('maxFragmentDualSrcAttachments', c_uint32),
        ('maxFragmentCombinedOutputResources', c_uint32),
        ('maxComputeSharedMemorySize', c_uint32),
        ('maxComputeWorkGroupCount', c_uint32 * 3),
        ('maxComputeWorkGroupInvocations', c_uint32),
        ('maxComputeWorkGroupSize', c_uint32 * 3),
        ('subPixelPrecisionBits', c_uint32),
        ('subTexelPrecisionBits', c_uint32),
        ('mipmapPrecisionBits', c_uint32),
        ('maxDrawIndexedIndexValue', c_uint32),
        ('maxDrawIndirectCount', c_uint32),
        ('maxSamplerLodBias', c_float),
        ('maxSamplerAnisotropy', c_float),
        ('maxViewports', c_uint32),
        ('maxViewportDimensions', c_uint32 * 2),
        ('viewportBoundsRange', c_float * 2),
        ('viewportSubPixelBits', c_uint32),
        ('minMemoryMapAlignment', c_size_t),
        ('minTexelBufferOffsetAlignment', VkDeviceSize),
        ('minUniformBufferOffsetAlignment', VkDeviceSize),
        ('minStorageBufferOffsetAlignment', VkDeviceSize),
        ('minTexelOffset', c_int32),
        ('maxTexelOffset', c_uint32),
        ('minTexelGatherOffset', c_int32),
        ('maxTexelGatherOffset', c_uint32),
        ('minInterpolationOffset', c_float),
        ('maxInterpolationOffset', c_float),
        ('subPixelInterpolationOffsetBits', c_uint32),
        ('maxFramebufferWidth', c_uint32),
        ('maxFramebufferHeight', c_uint32),
        ('maxFramebufferLayers', c_uint32),
        ('framebufferColorSampleCounts', VkSampleCountFlags),
        ('framebufferDepthSampleCounts', VkSampleCountFlags),
        ('framebufferStencilSampleCounts', VkSampleCountFlags),
        ('framebufferNoAttachmentsSampleCounts', VkSampleCountFlags),
        ('maxColorAttachments', c_uint32),
        ('sampledImageColorSampleCounts', VkSampleCountFlags),
        ('sampledImageIntegerSampleCounts', VkSampleCountFlags),
        ('sampledImageDepthSampleCounts', VkSampleCountFlags),
        ('sampledImageStencilSampleCounts', VkSampleCountFlags),
        ('storageImageSampleCounts', VkSampleCountFlags),
        ('maxSampleMaskWords', c_uint32),
        ('timestampComputeAndGraphics', VkBool32),
        ('timestampPeriod', c_float),
        ('maxClipDistances', c_uint32),
        ('maxCullDistances', c_uint32),
        ('maxCombinedClipAndCullDistances', c_uint32),
        ('discreteQueuePriorities', c_uint32),
        ('pointSizeRange', c_float * 2),
        ('lineWidthRange', c_float * 2),
        ('pointSizeGranularity', c_float),
        ('lineWidthGranularity', c_float),
        ('strictLines', VkBool32),
        ('standardSampleLocations', VkBool32),
        ('optimalBufferCopyOffsetAlignment', VkDeviceSize),
        ('optimalBufferCopyRowPitchAlignment', VkDeviceSize),
        ('nonCoherentAtomSize', VkDeviceSize),
    ]


# https://docs.vulkan.org/spec/latest/chapters/sparsemem.html#VkPhysicalDeviceSparseProperties
class VkPhysicalDeviceSparseProperties(Structure):
    _fields_ = [
        ('residencyStandard2DBlockShape', VkBool32),
        ('residencyStandard2DMultisampleBlockShape', VkBool32),
        ('residencyStandard3DBlockShape', VkBool32),
        ('residencyAlignedMipSize', VkBool32),
        ('residencyNonResidentStrict', VkBool32),
    ]


# https://docs.vulkan.org/spec/latest/chapters/devsandqueues.html#VK_MAX_PHYSICAL_DEVICE_NAME_SIZE
VK_MAX_PHYSICAL_DEVICE_NAME_SIZE = 256

# https://docs.vulkan.org/spec/latest/chapters/devsandqueues.html#VK_UUID_SIZE
VK_UUID_SIZE = 16


# https://docs.vulkan.org/spec/latest/chapters/devsandqueues.html#VkPhysicalDeviceProperties
class VkPhysicalDeviceProperties(Structure):
    _fields_ = [
        ('apiVersion', c_uint32),
        ('driverVersion', c_uint32),
        ('vendorID', c_uint32),
        ('deviceID', c_uint32),
        ('deviceType', c_int),
        ('deviceName', c_char * VK_MAX_PHYSICAL_DEVICE_NAME_SIZE),
        ('pipelineCacheUUID', c_uint8 * VK_UUID_SIZE),
        ('limits', VkPhysicalDeviceLimits),
        ('sparseProperties', VkPhysicalDeviceSparseProperties)
    ]


# https://docs.vulkan.org/spec/latest/chapters/devsandqueues.html#VkPhysicalDeviceProperties2
class VkPhysicalDeviceProperties2(Structure):
    _fields_ = [
        ('sType', c_int),
        ('pNext', c_void_p),
        ('properties', VkPhysicalDeviceProperties)
    ]


# https://docs.vulkan.org/refpages/latest/refpages/source/vkCreateInstance.html
vkCreateInstance = libvulkan.vkCreateInstance
vkCreateInstance.argtypes = [POINTER(VkInstanceCreateInfo), c_void_p, POINTER(c_void_p)]

# https://docs.vulkan.org/refpages/latest/refpages/source/vkDestroyInstance.html
vkDestroyInstance = libvulkan.vkDestroyInstance
vkDestroyInstance.argtypes = [c_void_p, c_void_p]

# https://docs.vulkan.org/refpages/latest/refpages/source/vkEnumeratePhysicalDevices.html
vkEnumeratePhysicalDevices = libvulkan.vkEnumeratePhysicalDevices
vkEnumeratePhysicalDevices.argtypes = [c_void_p, POINTER(c_uint32), POINTER(c_void_p)]

# https://docs.vulkan.org/spec/latest/chapters/devsandqueues.html#vkGetPhysicalDeviceProperties2
vkGetPhysicalDeviceProperties2 = libvulkan.vkGetPhysicalDeviceProperties2
vkGetPhysicalDeviceProperties2.argtypes = [c_void_p, POINTER(VkPhysicalDeviceProperties2)]

# https://docs.vulkan.org/spec/latest/chapters/extensions.html#extendingvulkan-coreversions-versionnumbers
VK_MAKE_VERSION = lambda major, minor, patch: ((major << 22) | (minor << 12) | patch)
