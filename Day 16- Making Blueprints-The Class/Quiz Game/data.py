# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 03:50:12 2025

@author: toora
"""

question_data= [
  {
    "question": "In 2008, Usain Bolt set the world record for the 100 meters with one shoelace untied.",
    "correct_answer": "True"
  },
  {
    "question": "Norwegian producer Kygo released a remix of the song \"Sexual Healing\" by Marvin Gaye.",
    "correct_answer": "True"
  },
  {
    "question": "There aren't any live-action clones in \"Star Wars: Episode III - Revenge of the Sith\".",
    "correct_answer": "True"
  },
  {
    "question": "In \"Overwatch,\" an allied McCree will say \"Step right up\" upon using his ultimate ability, Deadeye.",
    "correct_answer": "True"
  },
  {
    "question": "Coca-Cola's original color was green.",
    "correct_answer": "False"
  },
  {
    "question": "In \"JoJo's Bizarre Adventure,\" Father Enrico Pucci uses a total of three Stands in Part 6: Stone Ocean.",
    "correct_answer": "True"
  },
  {
    "question": "Pink Guy's debut album was \"Pink Season\".",
    "correct_answer": "False"
  },
  {
    "question": "Mortal Kombat was almost based on a Jean-Claude Van Damme movie.",
    "correct_answer": "True"
  },
  {
    "question": "The sum of all the numbers on a roulette wheel is 666.",
    "correct_answer": "True"
  },
  {
    "question": "When BMW was established in 1916, it was producing automobiles.",
    "correct_answer": "False"
  },
  {
    "question": "During the 2016 United States presidential election, the state of California possessed the most electoral votes, having 55.",
    "correct_answer": "True"
  },
  {
    "question": "Amazon acquired Twitch in August 2014 for $970 million.",
    "correct_answer": "True"
  },
  {
    "question": "In AMC's \"The Walking Dead,\" the characters Rick, Carl, Daryl, Morgan, Carol, and Maggie were introduced in Season 1.",
    "correct_answer": "False"
  },
  {
    "question": "SCP-173 was the first SCP article written for the web-based collaborative fiction project known as the \"SCP Foundation\".",
    "correct_answer": "True"
  },
  {
    "question": "In the webcomic Homestuck, the first character introduced is Dave Strider.",
    "correct_answer": "False"
  },
  {
    "question": "An episode of \"The Simpsons\" is dedicated to Moe Szyslak's bar rag.",
    "correct_answer": "True"
  },
  {
    "question": "Italy and Ireland are the only countries in Europe that start with the letter I.",
    "correct_answer": "False"
  },
  {
    "question": "A Boolean value of \"0\" represents \"false\".",
    "correct_answer": "False"
  },
  {
    "question": "The first Maxis game to feature the fictional language \"Simlish\" was The Sims (2000).",
    "correct_answer": "False"
  },
  {
    "question": "In Riot Games' \"League of Legends,\" the Halloween event is called \"The Reckoning\".",
    "correct_answer": "False"
  },
  {
    "question": "Sugar contains fat.",
    "correct_answer": "False"
  },
  {
    "question": "The vapor produced by e-cigarettes is actually water.",
    "correct_answer": "False"
  },
  {
    "question": "Route 66 in the United States spans the entire mainland from California to New York.",
    "correct_answer": "False"
  },
  {
    "question": "The term \"spam\" came before the food product \"Spam\".",
    "correct_answer": "False"
  },
  {
    "question": "You could walk from Norway to North Korea while only passing through Russia.",
    "correct_answer": "True"
  },
  {
    "question": "The open-source program Redis is a relational database server.",
    "correct_answer": "False"
  },
  {
    "question": "In \"Star Trek,\" Klingons are commonly referred to as \"Black Elves\".",
    "correct_answer": "False"
  },
  {
    "question": "Pure water effectively conducts electricity.",
    "correct_answer": "False"
  },
  {
    "question": "\"Windows NT\" is a monolithic kernel.",
    "correct_answer": "False"
  },
  {
    "question": "The Ace Attorney trilogy was supposed to end with \"Phoenix Wright: Ace Attorney – Trials and Tribulations\" as its final game.",
    "correct_answer": "True"
  },
  {
    "question": "The original ending of \"Little Shop of Horrors\" has the plants taking over the world.",
    "correct_answer": "True"
  },
  {
    "question": "United States President Ronald Reagan was the first president to appoint a woman to the Supreme Court.",
    "correct_answer": "True"
  },
  {
    "question": "The Pythagorean theorem states that the square of the hypotenuse is equal to the product of the squares of the other two sides.",
    "correct_answer": "False"
  },
  {
    "question": "Android versions are named in alphabetical order.",
    "correct_answer": "True"
  },
  {
    "question": "Assyrian King Sennacherib's destruction of Babylon in 689 BCE was viewed as a triumph by other Assyrian citizens.",
    "correct_answer": "False"
  },
  {
    "question": "Norway has a larger land area than Sweden.",
    "correct_answer": "False"
  },
  {
    "question": "Only a small percentage of the world's population is lactose intolerant.",
    "correct_answer": "False"
  },
  {
    "question": "\"Tachycardia\" or \"tachyarrhythmia\" refers to a resting heart rate near or over 100 BPM.",
    "correct_answer": "True"
  },
  {
    "question": "Rapper Snoop Dogg's real name is Cordozar Calvin Broadus Jr.",
    "correct_answer": "True"
  },
  {
    "question": "EDM label Monstercat signs tracks instead of artists.",
    "correct_answer": "True"
  },
  {
    "question": "The snowmobile was invented by Canadian Joseph-Armand Bombardier in 1937.",
    "correct_answer": "True"
  },
  {
    "question": "In the video game \"Transistor,\" Red is the name of the main character.",
    "correct_answer": "True"
  },
  {
    "question": "Ferrari has never made a V10 engine for any of its cars.",
    "correct_answer": "False"
  },
  {
    "question": "The animated film \"Spirited Away\" won the Academy Award for Best Animated Feature at the 75th Academy Awards in 2003.",
    "correct_answer": "True"
  },
  {
    "question": "The character that would eventually become Dr. Eggman was considered for Sega's mascot before Sonic.",
    "correct_answer": "True"
  },
  {
    "question": "Adolf Hitler was accepted into the Vienna Academy of Fine Arts.",
    "correct_answer": "False"
  },
  {
    "question": "The game Garry's Mod originally took assets and code from the Half-Life 2 mod JBmod.",
    "correct_answer": "True"
  },
  {
    "question": "Shang Tsung is a playable character in Mortal Kombat XL.",
    "correct_answer": "False"
  },
  {
    "question": "Where are Terror Fiends more commonly found in the Nintendo game Miitopia?",
    "correct_answer": "New Lumos"
  },
  {
    "question": "What is the capital of Slovakia?",
    "correct_answer": "Bratislava"
  },
  {
    "question": "The dish Fugu is made from what family of fish?",
    "correct_answer": "Pufferfish"
  },
  {
    "question": "Which British writer wrote for both Doctor Who and Sherlock?",
    "correct_answer": "Steven Moffat"
  },
  {
    "question": "The weapon Clint Eastwood uses in \"Dirty Harry\" was a .44 Automag.",
    "correct_answer": "False"
  },
  {
    "question": "In the first Left 4 Dead, which four characters can you play as?",
    "correct_answer": "Francis, Bill, Zoey, and Louis"
  },
  {
    "question": "What car manufacturer gave away their seat-belt patent to save lives?",
    "correct_answer": "Volvo"
  },
  {
    "question": "Who was SEGA's mascot before Sonic the Hedgehog?",
    "correct_answer": "Alex Kidd"
  },
  {
    "question": "Which internet company began as an online bookstore called \"Cadabra\"?",
    "correct_answer": "Amazon"
  },
  {
    "question": "At which bridge does the annual Oxford and Cambridge boat race start?",
    "correct_answer": "Putney"
  },
  {
    "question": "Three members of 2 Live Crew were arrested for playing songs from their album \"As Nasty As They Wanna Be\" live.",
    "correct_answer": "True"
  },
  {
    "question": "Which animation studio animated \"Hidamari Sketch\"?",
    "correct_answer": "Shaft"
  },
  {
    "question": "Which of these artists does not originate from France?",
    "correct_answer": "The Chemical Brothers"
  },
  {
    "question": "Which class of animals are newts members of?",
    "correct_answer": "Amphibian"
  },
  {
    "question": "In \"The Simpsons,\" what is the real name of Comic Book Guy?",
    "correct_answer": "Jeff Albertson"
  },
  {
    "question": "Which franchise had a special event hosted in Final Fantasy XIV: A Realm Reborn?",
    "correct_answer": "Yo-kai Watch"
  },
  {
    "question": "What English word means to \"think deeply\"?",
    "correct_answer": "Contemplate"
  },
  {
    "question": "Who was the leader of Sweden during the Great Northern War?",
    "correct_answer": "Charles XII"
  },
  {
    "question": "Alaska is the largest state in the United States.",
    "correct_answer": "True"
  },
  {
    "question": "Who was the 40th President of the United States?",
    "correct_answer": "Ronald Reagan"
  },
  {
    "question": "Which of the following card games revolves around numbers and basic math?",
    "correct_answer": "Uno"
  },
  {
    "question": "Dee from \"It's Always Sunny in Philadelphia\" has dated all of the following except one.",
    "correct_answer": "Matthew \"Rickety Cricket\" Mara"
  },
  {
    "question": "Denmark has a monarch.",
    "correct_answer": "True"
  },
  {
    "question": "Who is frozen at the end of the movie \"GoldenEye\"?",
    "correct_answer": "Boris Grishenko"
  },
  {
    "question": "In World of Warcraft lore, how many siblings does Sylvanas Windrunner have?",
    "correct_answer": "3"
  },
  {
    "question": "The main character of \"The Legend of Zelda\" is named Zelda.",
    "correct_answer": "False"
  },
  {
    "question": "Who is Sonic the Hedgehog's sidekick?",
    "correct_answer": "Tails"
  },
  {
    "question": "Boys Noize and Skrillex released music together under what name?",
    "correct_answer": "Dog Blood"
  },
  {
    "question": "In Greek mythology, Persephone had to return to the underworld after eating which seeds?",
    "correct_answer": "Pomegranate"
  },
  {
    "question": "What year did the anime \"Himouto! Umaru-chan\" air?",
    "correct_answer": "2015"
  },
  {
    "question": "In Java, which keyword prevents a variable from being modified?",
    "correct_answer": "Final"
  },
  {
    "question": "In \"Resident Evil 2,\" what is Leon Kennedy's middle name?",
    "correct_answer": "Scott"
  },
  {
    "question": "Panic! at the Disco's album \"Pray for the Wicked\" was released on June 22, 2018.",
    "correct_answer": "June 22, 2018"
  },
  {
    "question": "Which Avicii song samples \"Something's Got a Hold on Me\" by Etta James?",
    "correct_answer": "Levels"
  },
  {
    "question": "DragonForce's \"Through the Fire and Flames\" is considered the hardest song in Guitar Hero.",
    "correct_answer": "True"
  },
  {
    "question": "What is traditional haggis made of?",
    "correct_answer": "Sheep's heart, liver, and lungs"
  },
  {
    "question": "Who voices Shou Suzuki in the English dub of \"Mob Psycho 100\"?",
    "correct_answer": "Casey Mongillo"
  },
  {
    "question": "Which U.S. senator performed a 24-hour-long filibuster?",
    "correct_answer": "Strom Thurmond"
  },
  {
    "question": "In \"Kingdom Hearts,\" who abducts Jasmine in the Lamp Chamber?",
    "correct_answer": "Riku"
  },
  {
    "question": "Rannamaari was a sea demon from Maldivian folklore that required monthly sacrifices.",
    "correct_answer": "True"
  },
  {
    "question": "In WarioWare: Smooth Moves, which of these is not a Form?",
    "correct_answer": "The Hotshot"
  },
  {
    "question": "Augustus was the cousin of Julius Caesar.",
    "correct_answer": "False"
  },
  {
    "question": "Who was the first jazz musician to win the Pulitzer Prize for Music?",
    "correct_answer": "Wynton Marsalis"
  }
]
