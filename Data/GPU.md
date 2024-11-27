---
links:
  - "[[Artificial Intelligence]]"
aliases:
  - Graphics Processing Unit
---
 # GPU

https://book.premai.io/state-of-open-source-ai/hardware/#machine-learning-and-gpus

# Programming for GPUs & Low-level Optimization

Programming for NVIDIA, AMD, Intel hardware: CUDA. [RAPIDs](https://rapids.ai), GPGPU

## NVIDIA

### CUDA

### Vulkan

## AMD

For AMD GPUs, you can use the ROCm (Radeon Open Compute) platform, which is an open-source software platform for GPU-enabled HPC (High-Performance Computing) and machine learning applications.

## Apple Silicon

### Metal

### Metal Performance Shaders (MPS

## Cross Platform Graphics APIs

- Cross Platform Graphics APIs allow developers to ==harness== GPU power efficiently across different hardware and operating systems.
- ML Frameworks have intergrations with graphics API to optimize performance, especially for operations that can be parellelized on GPUs

### Vulkan

### OpenGL

### Metal

### OpenCL

**OpenCL** is a framework for writing programs that execute across heterogeneous platforms consisting of CPUs, GPUs, and other processors. OpenCL includes a language (based on C99) for writing kernels (i.e., functions that run on the hardware devices), plus APIs that are used to define and then control the platforms. OpenCL provides parallel computing using task-based and data-based parallelism.

## Acceleration Libraries

### Dedicated GPUs

CUDA is **a parallel computing platform and programming model developed by NVIDIA for general computing on graphical processing units (GPUs)**
The CUDA (Compute Unified Device Architecture) platform is a software framework developed by NVIDIA to **expand the capabilities of GPU acceleration**
Whether for the host computer or the GPU device, **all CUDA source code is now processed according to C++ syntax rules**
**CUDA is specifically designed for Nvidia's GPUs** however, OpenCL works on Nvidia and AMD's GPUs. OpenCL's code can be run on both GPU and CPU whilst CUDA's code is only executed on GPU.

### Parallel Computing 

https://analyticsindiamag.com/developers-corner/6-alternatives-to-cuda