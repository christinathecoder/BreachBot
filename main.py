breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook Data Breach.")


#Introduces breach
print("Would you like to learn about the Facebook 2019 Data Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Phone numbers, full names, locations, some email addresses, and other personal information of 533 million Facebook users in 106 countries was stolen in Facebook’s data breach in 2019. The hack was caused by malicious actors who were able to scrape data by exploiting a vulnerability that allowed users to find each other by phone numbers.")
  
  elif topic.lower() == "b":
    print("After the data breach, Facebook reached a $5 billion settlement with the U.S. Federal Trade Commission for violating an agreement to protect user privacy. Facebook made it clear that passwords, financial information, or health information were not part of the data breach.")
  
  elif topic.lower() == "c":
    break 
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("Attackers exploited a vulnerability to scrape the phone numbers, emails, and names of 533 million users.")
  
  elif topic.lower() == "b":
    print("We disagree with the organization's response because Facebook should have notified users to keep an eye out for any scams or other security issues. While Facebook defended its action by stating the scraped data was already public, failing to alert users prevented them from taking the needed steps to secure their compromised personal information.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by supporting them and encouraging them to keep an eye out for any unusual activities. My advice would be to immediately update passwords across their most sensitive accounts and freeze their cards.") 

  elif topic.lower() == "d":
    break 
    
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")