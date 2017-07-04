#

##Motivation
## The proposed memory simulator
To address the problem, we build a pin-based cycle-accurate flexible memory simulator on top of ramulator. It provides friendly memory access interface for hardware accelerator design and allows either fast simulation with lower accuracy or slower simulation with more accurate memory architecture simulation. As it is built on top of ramulator, a set of new memory architectures are also supported allowing the hardware accelerator exploration over the different memory architectures.

The simulator includes primitive memory model, profiling based simplified memory model and high level memory interfaces as well as memory content management. The primitive memory model is essentially the ramulator allowing cycle-accurate simulation. The profiling based simplified memory model ignores the low level memory architecture and provides only latency obtained through statistical results of a profling based on the ramulator. The memory interfaces is a pin-based interface providing various memory access manners such as stream memory access, burst memory access and random memory access widely used in hardware accelerator development. The memory content management automatically handles the memory image and ensures sequential consistency.

We may further add some other functionality in future:
1) power consumption model including both the memory and bus interface etc.
2) statistical information to assist the memory access bottleneck analysis

##Experiments
simulation speed and accuracy
