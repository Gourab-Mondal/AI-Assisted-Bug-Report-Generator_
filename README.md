# 🧪 AI-Generated Login Test Automation (SauceDemo)

This project demonstrates how **AI-assisted test design** can be combined with **Selenium automation** to validate login functionality on a real web application.

The target application used is:  
🔗 https://www.saucedemo.com


## 🎯 Objective

- Use AI to generate meaningful test cases for login functionality  
- Automate at least one test case using Selenium  
- Show how AI improves test design and coverage  



## 🤖 AI-Generated Login Test Cases

The following test cases were generated with the help of AI based on the login requirements of the application.

### Test Case 1 – Valid Login  
**Steps**
1. Open saucedemo.com  
2. Enter username: `standard_user`  
3. Enter password: `secret_sauce`  
4. Click Login  

**Expected Result**  
User should be redirected to the inventory page.


### Test Case 2 – Invalid Password  
**Steps**
1. Enter username: `standard_user`  
2. Enter password: `wrong_pass`  
3. Click Login  

**Expected Result**  
An error message should be displayed.


### Test Case 3 – Empty Fields  
**Steps**
1. Leave username and password blank  
2. Click Login  

**Expected Result**  
An error message indicating missing credentials.


### Test Case 4 – Locked Out User  
**Steps**
1. Enter username: `locked_out_user`  
2. Enter password: `secret_sauce`  
3. Click Login  

**Expected Result**  
Login should fail with a locked-out message.


### Test Case 5 – Username Case Sensitivity  
**Steps**
1. Enter username: `Standard_User`  
2. Enter password: `secret_sauce`  
3. Click Login  

**Expected Result**  
Login should fail due to case-sensitive username.

| TC ID | Scenario | Expected Result |
|------|---------|----------------|
| TC01 | Valid login | User lands on inventory page |
| TC02 | Invalid password | Error message is displayed |
| TC03 | Empty username | Validation error |
| TC04 | Empty password | Validation error |
| TC05 | Locked out user | Access denied message |

## 🧠 How AI Helped Test Design

Instead of manually guessing test cases, AI was used to generate a **balanced set of positive, negative, and edge-case scenarios**.

AI helped identify:
- Locked-out users  
- Case sensitivity issues  
- Missing input validation  
- Standard positive login flow  

This improved test coverage and reduced the chance of human bias while designing test scenarios.


## 🧪 Automated Test

The following test case was automated using Selenium:

> **Test Case 1 – Valid Login**

The script:
- Opens the website  
- Enters valid credentials  
- Clicks login  
- Verifies navigation to the inventory page  


## ⚙️ Tech Stack

- Python  
- Selenium WebDriver  
- Chrome Browser  


## ▶️ How to Run the Test

1. Clone the repository
```
git clone https://github.com/Gourab-Mondal/AI-Assisted-Bug-Report-Generator_
cd ai-assisted-bug-report-generator_
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the test
```
python test_login.py
```
If login is successful, you will see:
```
✅ Login Test Passed
```

## 📌 Notes

- This project demonstrates:

1. AI-assisted test design
2. Selenium-based UI automation
3. Practical QA thinking using a real application
