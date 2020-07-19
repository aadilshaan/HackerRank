# Binary Numbers

digital_no = int(input().strip())
dul_binary_no = str(bin(digital_no))
binary_no = dul_binary_no[2:]
length = [no for no in binary_no.split('0')]
print(len(max(length)))