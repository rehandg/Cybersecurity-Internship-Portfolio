# TASK_2-Phishing-Email-Analysis
This Task consists of a sample phishing email analysis and understand how this email is determined to be a phishing email.


Steps Performed in Order:

#1.Screenshots/Images Collected: here i took screenshots of a sample email from a website, there are two images of the whole email.
ABOUT THE EMAIL: This is a sample Phishing email , Here an anonymous sender is claiming to be from Netflix stating that receiver is having there "Password" expired in 3 days.the link given states "RESET PASSWORD" and in the end concludes the message with a threatening tone.




#2.Header Analysis: I used the Google message email header reader for analyzing the emails header and find the servers its passed through which reveales that the email is fake.

The EMAIL HEADER that i used:

Delivered-To: john.doe@mybusiness.com
Received: by mail.mybusiness.com with SMTP id x123456abc;
        Mon, 27 May 2025 19:45:00 +0000 (UTC)
Return-Path: <netflix@webnotifications.net>
Received: from suspicious-host.net ([203.0.113.55])
        by mail.mybusiness.com with ESMTP id x987654zyx;
        Mon, 27 May 2025 19:44:58 +0000 (UTC)
Date: Mon, 27 May 2025 19:44:58 +0000
From: Netflix Password Reset <netflix@webnotifications.net>
To: john.doe@mybusiness.com
Subject: Netflix password expiring in 3 days
Message-ID: <fakedmsgid123456@example.com>
MIME-Version: 1.0
Content-Type: text/html; charset="UTF-8"

i have uploaded a PNG and txt file of the header and the result of its analysis.

#3.Sender's Address:netflix@webnotifications.net this address is the fisrt sign that email if fake , the offcial netflix email address does not have webnotifications in it.


#4.Supscious_Link: the email then contains a link saying REST THE PASSWORD and upon opening the link it takes to a very untrusty looking web asking you to enter the account's credentials.
IF we go along with the flow and enter the account details then our account will be stolen.


#5.Grammar errors and Threatening TONE: the email has various mistakes and errors in sentences and address everything in a Threatening manner.

"Your password is due to expire in 3 days."

from the email.

All the given SUS traits are:

*Spoofing Sender's Address.

*Grammar and spelling mistakes.

*threatening Tone.

*Suspicious link leading to sus WEB Page upon opening

*Email Header analysis revealing sender and confirming that it's fake

Conclsion:
all the step by step analysis of the email concludes that the email is a threat and needs to be reported.


#all the emages and txt flies are uploaded.




