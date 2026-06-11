# Countdown Timer 
A terminal-based countdown timer that ticks every second and ends with a bang.

---

## 1. Description
- Language: Python
- Input: Time in seconds
- Output: Live countdown in MM:SS format
- Ends with: "Time Over!!" when timer hits 0

---

## 2. How It Works
1. User enters time in seconds
2. Timer converts seconds to MM:SS format using `divmod`
3. Countdown updates every second using `time.sleep(1)`
4. Prints over the same line using `\r`
5. Prints "Time Over!!" when done

---

## 3. Input / Output
| Scenario | Input | Output |
|---|---|---|
| Normal countdown | 90 | 01:30 → 01:29 → ... → 00:00 |
| Last second | 1 | 00:01 → "Boom!!" |
| Instant | 0 | "Boom!!" immediately |

---

## 4. Screenshot
<img width="1390" height="156" alt="Image" src="https://github.com/user-attachments/assets/af8aab6d-b0aa-49a5-b44f-ab6ab62bd2af" />
<img width="1452" height="152" alt="Image" src="https://github.com/user-attachments/assets/51e50664-33f7-44be-a2cb-aa7cd00e6ce3" />

---
