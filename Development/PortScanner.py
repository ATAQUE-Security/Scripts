# !/usr/bin/python3

# Script Name:                  Attack Tools Part 2 of 3
# Author:                       Raphael Chookagian
# Date of latest revision:      09/11/2023
# Purpose:                      Python script for Nmap Automation Tool
# This script is sourced from lab42 and demo code from [401d8-Github](https://github.com/codefellows/seattle-cybersecurity-401d8/blob/main/class-42/challenges/DEMO.md)

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""")
print("You have selected option: ", resp)

# range = '1-50'
range = input("Enter the port range to scan (e.g. 1-50): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'udp' in scanner[ip_addr].all_protocols():
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    else:
        print("No UDP ports found open.")
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'tcp' in scanner[ip_addr].all_protocols():
        print("Open TCP Ports: ", scanner[ip_addr]['tcp'].keys())
    if 'udp' in scanner[ip_addr].all_protocols():
        print("Open UDP Ports: ", scanner[ip_addr]['udp'].keys())
elif resp >= '4':
    print("Please enter a valid option")
