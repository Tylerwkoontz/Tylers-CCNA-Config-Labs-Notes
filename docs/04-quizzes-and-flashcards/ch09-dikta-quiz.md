# Chapter 09 "Do I Know This Already?" (DIKTA) Quiz

Test your readiness for Chapter 9 concepts before or after reading.

---

### Question 1
Which of the following subnet masks provides at least 50 usable host IP addresses per subnet while maximizing the number of remaining subnets in a Class C network?
- [ ] A) `255.255.255.128` (/25)
- [x] B) `255.255.255.192` (/26)  *(Correct: provides 62 usable hosts)*
- [ ] C) `255.255.255.224` (/27)
- [ ] D) `255.255.255.240` (/28)

---

### Question 2
What is the broadcast address for the subnet containing the host `172.20.99.45/19`?
- [ ] A) `172.20.99.255`
- [ ] B) `172.20.127.255`
- [x] C) `172.20.127.255` *(Correct: 3rd octet magic number is 32; subnet is 172.20.96.0, broadcast is 172.20.127.255)*
- [ ] D) `172.20.111.255`

---

### Question 3
In Cisco IOS, when an interface is configured with `ip address 10.1.1.1 255.255.255.0` and brought up, what two route types appear in `show ip route`?
- [x] **Connected (`C`)**: `10.1.1.0/24`
- [x] **Local (`L`)**: `10.1.1.1/32`
