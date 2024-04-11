# Time Lag based Side Channel Analysis 

Internal operations in microprocessor or microcontrolled can be disclosed with side channel analysis by various methods. In this experimental project, I am trying to extract password from an microcontroller by calculating response time for validation. 

When a password is entered for authentication, check is being done on each character. This includes using loops to itterate over them. Each itteration takes some ammount of time.

Hence, more right the password is, more time it will take for responding. This behavious is exploited to guess the password for authentication. 

Rather than bruteforce approach, this method reduces time significantly. 

If the password is n characters long consisting of m different characters, then: 

Side Channel Analysis (Time Lag Calculation): $m \times n$ attempts.

Bruteforce: $m^n$.

Attempts reduced to: $m \times n \div m^n \time 100$% 


