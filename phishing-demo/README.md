# Phishing Demo — Credential Harvesting Lab

## Overview
A controlled phishing simulation using the Social Engineering Toolkit (SET) 
on Kali Linux to understand how credential harvesting attacks work.

## Tools Used
- Kali Linux
- Social Engineering Toolkit (SET) v8.0.3
- Apache (port 80)

## What I Did
1. Launched SET → Social Engineering Attacks → Website Attack Vectors
2. Selected Credential Harvester → Site Cloner
3. Cloned a login page and hosted it locally on 10.0.2.15
4. Visited the cloned page — SET immediately captured session data, 
   tracking tokens, and POST parameters in real time

## Key Learning
- A cloned phishing page is indistinguishable visually from the real site
- Data is captured the moment the page loads — before credentials are entered
- Session tokens and telemetry leak immediately on page visit
- This is exactly how real attackers operate in credential harvesting campaigns

## Defense Takeaways
- Always verify the URL before entering credentials
- Password managers won't autofill on fake domains
- Enable 2FA — stolen passwords alone aren't enough
- Check for HTTPS + valid certificate

## Ethical Note
This was conducted in a controlled local environment for educational 
purposes only. No real credentials were harvested.

**Date:** May 1, 2026  
**Author:** Nilanjan Chowdhury
