How to manually disable ASLR
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
