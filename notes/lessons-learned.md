# CCNA Study Log & Lessons Learned

Record tricky insights, mnemonic devices, command differences, and personal takeaways here.

---

## 📌 Recent Insights

### 1. Subnetting Magic Number Trick
* Whenever calculating subnets, identify the **interesting octet** (the octet where the mask is neither 255 nor 0).
* Subtract that octet value from 256. The result is the step size for your subnets.
* *Example*: `/28` mask is `.240`. $256 - 240 = 16$. Subnets start at `.0`, `.16`, `.32`, `.48`...

### 2. Connected (`C`) vs Local (`L`) Routes
* Cisco IOS 15+ introduces `L` routes in the routing table.
* `C` represents the entire subnet connected to the interface.
* `L` is a `/32` host route pointing to the router's own interface IP for efficient packet processing destined to the control plane.
