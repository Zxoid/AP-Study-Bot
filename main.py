import os
import discord
from discord.ext import commands
import asyncio

token = "DISCORD_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def aphelp(ctx):
    await ctx.send("""
What do you want to study?
1. `!APWORLD`
2. `!APUSH`
3. `!APPSYCH`
4. `!APPRECALC`
5. `!APLANG`
6. `!APLIT`
7. `!APBIO`
8. `!APCHEM`
9. `!APPHYSICS1`
10. `!APES`
11. `!APCSA`
12. `!APCSP`
13. `!APSTATS`
    """)
    await asyncio.sleep(1)



# Command for AP World History study topics
@bot.command()
async def APWORLD(ctx):
    await ctx.send(
        """📚 **AP World History: Modern Topics to Study** (c. 1200 - Present):
1. **Mongol Empire & Globalization** - The rise of the Mongols and the expansion of trade routes.
2. **Renaissance and Reformation** - Key figures like Martin Luther and the impact on Europe.
3. **Age of Exploration** - Columbus, Vasco da Gama, and the impact of European exploration.
4. **The Enlightenment** - Major thinkers and ideas that influenced revolutions.
5. **Revolutions** - The American Revolution, French Revolution, Haitian Revolution, Latin American revolutions.
6. **Industrial Revolution** - Its global impact, from Britain to the rest of the world.
7. **World Wars** - World War I, World War II, and their global impacts.
8. **Cold War** - Key events, conflicts, and ideological tensions between the U.S. and the USSR.
9. **Decolonization** - The process of African and Asian countries gaining independence post-WWII.
10. **Globalization** - Economic, cultural, and political changes in the 20th and 21st centuries.
Type `!modernquizlets` to see flashcards!
Type `!moderndates` to see important dates to remember!
Type `!modernleaders` to see important figures to remember!
Type `!moderntraderoutes` to see important trade routes to remember!
Type `!modernconflicts` to see important conflicts to remember!
Type `!modernstudyguide` to get access to an exclusive study guide!
""")
    await asyncio.sleep(1)


@bot.command()
async def modernquizlets(ctx):
    await ctx.send(
        "Here is the full AP WORLD HISTORY: MODERN FLASHCARDS https://quizlet.com/user/quizlette83690296/folders/ap-world-history"
    )


@bot.command()
async def moderndates(ctx):
    await ctx.send("""📅 **AP World History: Modern - Important Dates**

**c.1200-c.1450:GlobalTapestry&NetworksofExchange**
**1206**:Genghis Khan unites Mongol tribes  
**1258**:Mongols sack Baghdad  
**1271**:Marco Polo travels to China  
**1324**:Mansa Musa pilgrimage to Mecca  
**1347-1351**:Black Death spreads across Eurasia  
**1368**:Fall of Yuan, rise of Ming  

**c.1450-c.1750:Renaissance,Exploration,Empires**  
**1453**:Fall of Constantinople  
**1492**:Columbus' voyage to Americas  
**1498**:Vasco da Gama reaches India  
**1517**:Martin Luther's 95 Theses  
**1521**:Spanish conquest of Aztec Empire  
**1600**:British East India Company established  
**1644**:Start of Qing Dynasty  
**1683**:Ottoman siege of Vienna  

**c.1750-c.1900:Revolutions,Industrialization,Imperialism**  
**1750**:Start of Industrial Revolution  
**1776**:American Declaration of Independence  
**1789**:Start of French Revolution  
**1804**:Haitian Independence  
**1839-1842**:First Opium War  
**1853**:Commodore Perry opens Japan  
**1857**:Indian Sepoy Mutiny  
**1884-1885**:Berlin Conference  
**1898**:Spanish-American War  

**c.1900-Present:GlobalConflict&ModernDevelopments**  
**1914-1918**:World War I  
**1917**:Russian Revolution  
**1939-1945**:World War II  
**1947**:India and Pakistan independence  
**1949**:Chinese Communist Revolution  
**1960s**:African Decolonization  
**1989**:Fall of Berlin Wall  
**1991**:Collapse of Soviet Union  
**2001**:9/11 Attacks  
**2008**:Global Financial Crisis  
**2011**:Arab Spring  
""")
    await asyncio.sleep(1)


import asyncio


@bot.command()
async def modernleaders(ctx):
    await ctx.send(
        """👥 **AP World History: Modern - Important Leaders (Part 1)**

    c.1200-c.1450: Global Tapestry & Networks of Exchange
    - Genghis Khan: United the Mongol tribes, creating the largest contiguous empire in history.
    - Kublai Khan: Grandson of Genghis, established the Yuan Dynasty in China.
    - Marco Polo: Venetian merchant who traveled to China, documenting his journey.
    - Mansa Musa: Wealthy ruler of the Mali Empire, known for his pilgrimage to Mecca.
    - Ibn Battuta: Moroccan explorer who traveled extensively throughout the Islamic world.
    
    --- Next part coming soon...""")
    await asyncio.sleep(1)
    await ctx.send(
        """👥 **AP World History: Modern - Important Leaders (Part 2)**

    c.1450-c.1750: Renaissance, Exploration, Empires
    - Christopher Columbus: Initiated European contact with the Americas (1492).
    - Vasco da Gama: First European to reach India by sea, opening maritime trade routes.
    - Martin Luther: Sparked the Protestant Reformation with his 95 Theses.
    - Akbar the Great: Mughal emperor noted for religious tolerance and administrative reforms.
    - Suleiman the Magnificent: Ottoman sultan who expanded the empire and reformed the legal system.
    - Hernán Cortés: Conquistador who led the conquest of the Aztec Empire.
    - Ivan the Terrible: First czar of Russia, known for centralizing power.

    --- Next part coming soon...""")
    await asyncio.sleep(1)

    await ctx.send(
        """👥 **AP World History: Modern - Important Leaders (Part 3)**

    c.1750-c.1900: Revolutions, Industrialization, Imperialism
    - George Washington: Leader of the American Revolution and first U.S. president.
    - Napoleon Bonaparte: French military leader who rose to power after the French Revolution.
    - Simon Bolivar: Revolutionary leader who played a key role in Latin American independence.
    - Karl Marx: Co-author of the Communist Manifesto, theorizing class struggle.
    - Queen Victoria: Symbol of British imperialism during the 19th century.
    - Cecil Rhodes: British imperialist and businessman involved in South Africa.
    - King Leopold II: Belgian king notorious for his brutal colonization of the Congo.

    --- Next part coming soon...""")
    await asyncio.sleep(1)

    await ctx.send(
        """👥 **AP World History: Modern - Important Leaders (Part 4)**

    c.1900-Present: Global Conflict & Modern Developments
    - Vladimir Lenin: Leader of the Russian Revolution and founder of the Soviet Union.
    - Mahatma Gandhi: Led India's nonviolent struggle for independence.
    - Adolf Hitler: Nazi leader responsible for World War II and the Holocaust.
    - Winston Churchill: British Prime Minister during World War II.
    - Joseph Stalin: Soviet leader known for industrialization and the Great Purge.
    - Nelson Mandela: Anti-apartheid revolutionary, first black President of South Africa.
    - Mao Zedong: Leader of the Chinese Communist Revolution.
    """)


@bot.command()
async def moderntraderoutes(ctx):
    await ctx.send("""🌍 **AP World History: Modern Trade Routes**
    
**1. The Silk Roads** - The ancient overland trade network connecting East Asia, Central Asia, and Europe. It facilitated the exchange of goods, cultures, and ideas.
    
**2. The Indian Ocean Trade Network**- A sea-based route connecting East Africa, the Arabian Peninsula, South Asia, and Southeast Asia. It was crucial for the exchange of goods like spices, textiles, and gold
    
 **3. Trans-Saharan Trade Routes**
- Land routes across the Sahara Desert connecting West Africa with the Mediterranean and the Middle East. Key for the trade of gold, salt, and other resources.
""")
    await asyncio.sleep(1)


@bot.command()
async def modernconflicts(ctx):
    part_1 = """🌍 **AP World History: Modern Conflicts**

    1. The American Revolution (1775-1783)
    A colonial revolt against British rule in the Thirteen American Colonies, leading to the creation of the United States.

    2. The French Revolution (1789-1799)
    A period of radical social and political upheaval in France that overthrew the monarchy and led to the rise of Napoleon Bonaparte.

    3. The Haitian Revolution (1791-1804)
    A successful slave revolt in the French colony of Saint-Domingue, leading to the establishment of the independent nation of Haiti.

    4. The Napoleonic Wars (1803-1815)
    A series of wars involving Napoleon Bonaparte’s French Empire and various European coalitions, significantly reshaping Europe’s political landscape.

    5. The Latin American Revolutions (1808-1825)
    A series of uprisings across Latin America, led by figures like Simón Bolívar, José de San Martín, and Miguel Hidalgo, against Spanish and Portuguese colonial rule."""

    await ctx.send(part_1)

    await asyncio.sleep(1)

    part_2 = """6. The Opium Wars (1839-1842; 1856-1860)
    Conflicts between China and Britain (and later France), primarily over the trade of opium, which led to the Treaty of Nanjing and the opening of China to foreign influence.

    7. The Taiping Rebellion (1850-1864)
    A massive civil war in southern China led by the Taiping Heavenly Kingdom, challenging the Qing Dynasty and resulting in millions of deaths.

    8. The Crimean War (1853-1856)
    A conflict between the Russian Empire and an alliance of the Ottoman Empire, France, Britain, and Sardinia, primarily over control of territory in the Black Sea region.

    9. The American Civil War (1861-1865)
    A conflict between the Northern states (Union) and Southern states (Confederacy) in the U.S., primarily over slavery and states' rights, which led to the abolition of slavery.

    10. The Boxer Rebellion (1899-1901)
    An anti-foreign, anti-Christian uprising in China, led by the "Boxers," which sought to expel foreign influence from China."""

    await ctx.send(part_2)

    await asyncio.sleep(1)

    part_3 = """11. World War I (1914-1918)
    A global conflict involving most of Europe, the U.S., and other powers, triggered by the assassination of Archduke Franz Ferdinand, leading to the downfall of several empires.

    12. World War II (1939-1945)
    A global war involving most of the world’s nations, marked by the Axis Powers (Germany, Italy, Japan) against the Allies (United States, Soviet Union, UK, and others). It resulted in significant political and territorial changes.

    13. The Chinese Civil War (1927-1950)
    A conflict between the Chinese Nationalist Party (Kuomintang) and the Communist Party of China, which ended with the establishment of the People's Republic of China under Mao Zedong.

    14. The Korean War (1950-1953)
    A conflict between North Korea (with Chinese and Soviet support) and South Korea (with United Nations and U.S. support) over ideological and territorial control of Korea.

    15. The Vietnam War (1955-1975)
    A conflict between communist North Vietnam (supported by the Soviet Union and China) and South Vietnam (backed by the United States), resulting in the fall of Saigon and the unification of Vietnam under communist rule."""

    await ctx.send(part_3)

    await asyncio.sleep(1)

    part_4 = """16. The Cold War (1947-1991)
    The prolonged geopolitical, ideological, and economic rivalry between the United States and the Soviet Union, including proxy wars like the Korean War, Vietnam War, and the Cuban Missile Crisis.

    17. The Gulf War (1990-1991)
    A conflict in which a coalition of countries led by the United States expelled Iraqi forces from Kuwait, following Iraq’s invasion of Kuwait.

    18. The Rwandan Genocide (1994)
    A mass killing of approximately 800,000 Tutsis and moderate Hutus by Hutu extremists in Rwanda, which occurred in a context of long-standing ethnic tension."""

    await ctx.send(part_4)


@bot.command()
async def modernstudyguide(ctx):
    await ctx.send(
        "**Here is the full AP WORLD HISTORY: MODERN STUDY GUIDE** https://uploads-ssl.webflow.com/605fe570e5454a357d1e1811/609f602ab8c522d2fbb74495_SS-AP-World-History.pdf"
    )


#Command for APUSH study topics
@bot.command()
async def APUSH(ctx):
    await ctx.send("""📚 **AP U.S. History Topics to Study** (c. 1491 - Present)

1. **Colonial America**: Exploration, colonization, and interactions between Native Americans and Europeans.
2. **American Revolution**: Causes, key battles, and the establishment of the United States.
3. **The Constitution and Early Republic**: The Articles of Confederation, the drafting of the Constitution, and the Federalist era.
4. **Expansion and Reform (1800-1860)**: Westward expansion, Manifest Destiny, and social reform movements.
5. **Civil War and Reconstruction**: Causes of the Civil War, major battles, and the challenges of rebuilding the South.
6.** Industrialization and Urbanization**: Rise of factories, labor movements, and the Gilded Age.
7. **The Progressive Era**: Social, political, and economic reforms addressing industrialization’s effects.
8.** The World Wars**: U.S. involvement in WWI and WWII, including the home front and global impact.
9. **The Great Depression and New Deal**: Causes, effects, and FDR’s policies to address the economic crisis.
10. **The Cold War**: U.S.-Soviet tensions, key events like the Korean and Vietnam Wars, and the policy of containment.
11. **Civil Rights Movement**: Key figures and milestones in the fight for racial and social justice.
12. **Modern America (1970s - Present)**: Political, social, and economic changes, including globalization and contemporary issues.

Type `!apushquizlets` to see flashcards!
Type `!apushdates` to see important dates to remember!
Type `!apushleaders` to see important figures to remember!
Type `!apushdocuments` to see important primary documents to remember!
Type `!apushconflicts` to see important conflicts to remember!
Type `!apushstudyguide` to get access to an exclusive study guide!""")
    await asyncio.sleep(1)


@bot.command()
async def apushquizlets(ctx):
    await ctx.send(
        "Here is the full APUSH FLASHCARDS https://quizlet.com/user/quizlette83690296/folders/ap-united-states-history?funnelUUID=c137f4e6-8d9b-46be-883d-76ff15bc2312"
    )


@bot.command()
async def apushdates(ctx):
    part_1 = """📅 **Important APUSH Dates**
**Colonial America (1491-1754)**
1492: Columbus arrives in the Americas.
1607: Founding of Jamestown, the first permanent English colony.
1620: Pilgrims establish Plymouth Colony.
1676: Bacon’s Rebellion in Virginia.
1692: Salem Witch Trials in Massachusetts.
**Revolutionary Era (1754-1800)**
1754-1763: French and Indian War.
1765: Stamp Act passed, sparking protests.
1770: Boston Massacre.
1773: Boston Tea Party.
1775-1783: American Revolutionary War.
1776: Declaration of Independence signed.
1781: Articles of Confederation ratified.
1787: U.S. Constitution drafted.
1789: George Washington becomes the first U.S. president.
1791: Bill of Rights ratified.
1793: Cotton gin invented by Eli Whitney."""
    await ctx.send(part_1)

    part_2 = """**Expansion and Reform (1800-1848)**
1803: Louisiana Purchase.
1807: Embargo Act.
1812-1815: War of 1812.
1820: Missouri Compromise.
1823: Monroe Doctrine issued.
1830: Indian Removal Act signed.
1848: Seneca Falls Convention (women’s rights).
**Civil War and Reconstruction (1844-1877)**
1848: Treaty of Guadalupe Hidalgo ends the Mexican-American War.
1850: Compromise of 1850.
1854: Kansas-Nebraska Act.
1861-1865: Civil War.
1863: Emancipation Proclamation.
1865: Assassination of Abraham Lincoln; 13th Amendment abolishes slavery.
1868: 14th Amendment grants citizenship rights.
1877: Compromise of 1877 ends Reconstruction."""
    await ctx.send(part_2)

    part_3 = """**Industrialization and Urbanization (1865-1898)**
1887: Dawes Act.
1890: Sherman Antitrust Act.
1896: Plessy v. Ferguson establishes "separate but equal."
1898: Spanish-American War.
**Progressive Era and World Wars (1890-1945)**
1901: Theodore Roosevelt becomes president.
1914-1918: World War I.
1920: 19th Amendment grants women the right to vote.
1929: Stock Market Crash; Great Depression begins.
1933: New Deal programs begin.
1941: Pearl Harbor attack; U.S. enters World War II.
1945: End of World War II; United Nations founded."""
    await ctx.send(part_3)

    part_4 = """**Cold War and Modern America (1945-Present)**
1947: Truman Doctrine.
1954: Brown v. Board of Education ends segregation in schools.
1964: Civil Rights Act passed.
1965: Voting Rights Act passed.
1973: U.S. withdraws from Vietnam; Roe v. Wade legalizes abortion.
1980: Ronald Reagan elected president.
1991: Soviet Union collapses; Cold War ends.
2001: September 11 terrorist attacks.
2008: Barack Obama elected as the first Black U.S. president.
2020: COVID-19 pandemic begins."""
    await ctx.send(part_4)


@bot.command()
async def apushleaders(ctx):
    part_1 = """👥 **Important APUSH Leaders**
**Colonial America (1491-1754)**
- John Smith: English soldier and explorer; helped establish the Jamestown colony.
- Pocahontas: Native American who played a key role in relations with Jamestown.
- William Bradford: Governor of Plymouth Colony and leader of the Pilgrims.
**Revolutionary Era (1754-1800)**
- George Washington: Commander-in-chief during the American Revolution and first U.S. president.
- Thomas Jefferson: Author of the Declaration of Independence and third U.S. president.
- Benjamin Franklin: Diplomat and Founding Father who helped secure French support during the Revolution.
- Alexander Hamilton: First U.S. Secretary of the Treasury; creator of financial systems."""
    await ctx.send(part_1)

    part_2 = """**Expansion and Reform (1800-1848)**
- Andrew Jackson: Seventh U.S. president, known for his populist policies and the Indian Removal Act.
- James K. Polk: 11th U.S. president, oversaw the Mexican-American War and territorial expansion.
- Harriet Tubman: Abolitionist and conductor on the Underground Railroad.
**Civil War and Reconstruction (1844-1877)**
- Abraham Lincoln: 16th U.S. president; led the country through the Civil War and issued the Emancipation Proclamation.
- Ulysses S. Grant: Union general and 18th U.S. president, led the North to victory in the Civil War.
- Robert E. Lee: General of the Confederate Army during the Civil War.
- Frederick Douglass: Former enslaved person, abolitionist leader, and advocate for civil rights.
**Progressive Era and World Wars (1890-1945)**
- Theodore Roosevelt: 26th U.S. president, known for his Progressive policies and trust-busting.
- Woodrow Wilson: 28th U.S. president, led the country during World War I and proposed the League of Nations.
- Franklin D. Roosevelt: 32nd U.S. president, led the country through the Great Depression and World War II.
**Cold War and Modern America (1945-Present)**
- Dwight D. Eisenhower: 34th U.S. president and World War II general.
- Martin Luther King Jr.: Civil rights leader who advocated for nonviolent resistance.
- Ronald Reagan: 40th U.S. president, known for his conservative policies and the end of the Cold War.
"""
    await ctx.send(part_2)


@bot.command()
async def apushdocuments(ctx):
    # Part 1: Colonial America (1491-1754)
    part_1 = """📜 **Colonial America (1491-1754)**
1. **Mayflower Compact (1620)**
   - The agreement signed by the Pilgrims aboard the Mayflower, establishing a self-governing colony.

2. **John Winthrop’s “City upon a Hill” (1630)**
   - A sermon by John Winthrop, offering a vision for the Massachusetts Bay Colony as a model Christian society.

3. **The Fundamental Orders of Connecticut (1639)**
   - The first written constitution in the American colonies, establishing a framework for government in Connecticut.
"""
    await ctx.send(part_1)

    # Part 2: Revolutionary Era (1754-1800)
    part_2 = """📜 **Revolutionary Era (1754-1800)**
1. **The Declaration of Independence (1776)**
   - A document declaring the colonies’ independence from Great Britain, written primarily by Thomas Jefferson.

2. **Common Sense by Thomas Paine (1776)**
   - A pamphlet advocating for independence from Britain and the establishment of a republic.

3. **The Federalist Papers (1787-1788)**
   - A series of essays written by Alexander Hamilton, James Madison, and John Jay, arguing for the ratification of the U.S. Constitution.

4. **Treaty of Paris (1783)**
   - The treaty that officially ended the Revolutionary War and recognized American independence.
"""
    await ctx.send(part_2)

    # Part 3: Expansion and Reform (1800-1848)
    part_3 = """📜 **Expansion and Reform (1800-1848)**
1. **Thomas Jefferson’s Inaugural Address (1801)**
   - Jefferson's speech outlining his vision for a limited federal government and national unity.

2. **The Monroe Doctrine (1823)**
   - A statement declaring that European powers should not interfere in the Americas, establishing a policy of U.S. dominance in the Western Hemisphere.

3. **Seneca Falls Declaration of Sentiments (1848)**
   - The foundational document of the women’s rights movement, calling for equal rights for women, including the right to vote.
"""
    await ctx.send(part_3)

    # Part 4: Civil War and Reconstruction (1844-1877)
    part_4 = """📜 **Civil War and Reconstruction (1844-1877)**
1. **The Emancipation Proclamation (1863)**
   - An executive order by Abraham Lincoln declaring all slaves in Confederate-held territory to be free.

2. **The Gettysburg Address (1863)**
   - Lincoln’s brief but powerful speech at the site of the Battle of Gettysburg, redefining the purpose of the war and American democracy.

3. **The 13th, 14th, and 15th Amendments**
   - The Reconstruction Amendments, which abolished slavery, granted citizenship to former slaves, and ensured voting rights regardless of race.

4. **Frederick Douglass’ “What to the Slave is the Fourth of July?” (1852)**
   - A speech in which Douglass criticizes the hypocrisy of celebrating liberty while slavery exists in the U.S.
"""
    await ctx.send(part_4)

    # Part 5: Gilded Age and Progressive Era (1877-1920)
    part_5 = """📜 **Gilded Age and Progressive Era (1877-1920)**
1. **The Populist Party Platform (1892)**
   - A document outlining the political agenda of the Populist Party, including demands for monetary reform and support for farmers and workers.

2. **The Social Gospel Movement (Late 19th Century)**
   - A series of sermons and writings by religious leaders advocating for social justice and reforms, including labor rights and the abolition of child labor.

3. **The 19th Amendment (1920)**
   - The amendment that granted women the right to vote, marking a significant victory in the women’s suffrage movement.
"""
    await ctx.send(part_5)

    # Part 6: World War I and the Interwar Period (1914-1941)
    part_6 = """📜 **World War I and the Interwar Period (1914-1941)**
1. **Woodrow Wilson’s 14 Points (1918)**
   - A statement of principles for peace negotiations to end World War I, including calls for free trade, self-determination, and the creation of the League of Nations.

2. **The Treaty of Versailles (1919)**
   - The peace treaty that ended World War I and imposed heavy reparations on Germany.

3. **Franklin D. Roosevelt’s First Inaugural Address (1933)**
   - A speech in which FDR declared war on the Great Depression, promising bold action and relief programs.
"""
    await ctx.send(part_6)

    # Part 7: World War II and Cold War (1941-1989)
    part_7 = """📜 **World War II and Cold War (1941-1989)**
1. **The Atlantic Charter (1941)**
   - A joint declaration between the U.S. and the UK, outlining the goals for the post-war world, including self-determination and free trade.

2. **Executive Order 9066 (1942)**
   - The order that authorized the internment of Japanese Americans during World War II.

3. **Truman Doctrine (1947)**
   - A policy statement by President Truman, committing the U.S. to support countries resisting communism, marking the start of the Cold War.

4. **The Civil Rights Act (1964)**
   - Landmark legislation that banned discrimination based on race, color, religion, sex, or national origin, ending segregation in public places.
"""
    await ctx.send(part_7)

    # Part 8: Modern America (1990-Present)
    part_8 = """📜 **Modern America (1990-Present)**
1. **Bill Clinton’s 1994 Crime Bill**
   - Legislation focused on combating crime, including provisions for the expansion of the prison system and the implementation of tougher law enforcement policies.

2. **The USA PATRIOT Act (2001)**
   - Legislation passed after the September 11 attacks, increasing law enforcement powers to combat terrorism.

3. **Obama’s 2009 Inaugural Address**
   - A speech calling for unity and bold action to overcome the economic and social challenges facing the nation.
"""
    await ctx.send(part_8)


@bot.command()
async def apushconflicts(ctx):
    part_1 = ("""🌍 **APUSH Conflicts**
    1. **Colonial & Early Wars**
    **King Philip’s War (1675-1676)**: A devastating conflict between Native American tribes and English colonists in New England.
    **French and Indian War (1754-1763)**: Fought between Britain and France (with Native American alliances on both sides), it led to British control over much of North America but also set the stage for colonial unrest.
    2. **American Revolution (1775-1783)
    A war between the Thirteen American Colonies and Britain, driven by tensions over taxes, representation, and British control. The colonies gained independence with the Treaty of Paris (1783).
    3. **War of 1812 (1812-1815)**
    Fought between the United States and Britain, partly over maritime rights, impressment of American sailors, and British support of Native American resistance. It ended in a stalemate but boosted U.S. nationalism.
    4. **Mexican-American War (1846-1848)**
    Sparked by territorial disputes after the annexation of Texas, this war resulted in the U.S. acquiring large parts of the Southwest (Treaty of Guadalupe Hidalgo).
    5. **American Civil War (1861-1865)**
    The most devastating conflict in U.S. history, fought between the Northern Union states and the Southern Confederacy. The war was primarily about slavery, states' rights, and economic differences. The Union's victory preserved the United States and ended slavery.
    """)
    await ctx.send(part_1)

    part_2 = (
        """6.** Spanish-American War (1898)** A brief war between Spain and the United States, triggered by the explosion of the USS Maine in Havana Harbor. The U.S. defeated Spain, gaining control of Puerto Rico, Guam, and the Philippines, marking the U.S. as a world power. 
7.** World War I (1917-1918)** The U.S. entered the war late, joining the Allies against the Central Powers. The conflict reshaped the global balance of power and set the stage for WWII.
8.** World War II (1941-1945)** A global conflict in which the U.S. joined the Allies after the Japanese attack on Pearl Harbor in 1941. The U.S. played a decisive role in defeating the Axis Powers, with the war ending in the defeat of Germany and Japan in 1945
9. **Korean War (1950-1953)** A conflict between North Korea (supported by China and the Soviet Union) and South Korea (backed by the United Nations and the U.S.). It ended with an armstistice.
10. **Vietnam War (1955-1975)** A prolonged conflict between communist North Vietnam (supported by China and the Soviet Union) and non-communist South Vietnam (backed by the U.S.). It ended with the fall of Saigon and the unification of Vietnam under communist rule. 
11.** Persian Gulf War (1990-1991)** Following Iraqs invasion of Kuwait, the U.S. led a coalition of nations in a swift military campaign (Operation Desert Storm) to drive Iraqi forces out of Kuwait. 
""")
    await ctx.send(part_2)


@bot.command()
async def apushstudyguide(ctx):
    await ctx.send(
        "**Here is the full APUSH STUDY GUIDE** https://www.tomrichey.net/uploads/3/2/1/0/32100773/apush_study_guide.pdf"
    )


#Command for APPSYCH study topics


@bot.command()
async def APPSYCH(ctx):
    await ctx.send("""📚 **AP Psychology Topics to Study** 
    1. **Biological Bases of Behavior** : The nervous system, hormones, and genetics,Learning and Memory
 2. **Cognition** : Sensation and Perception, Learning and Memory, Thinking and Intelligence
3. **Development and Learning** :Developmental stages, Learning theories
4. **Social Psychology and Personality**: Personality theories, Social influences on behavior
5. **Mental and Physical Health**: Stress and coping, Mental disorders, Physical health and behavior
    Type `!psychquizlets` to see flashcards!
    Type `!psychtheories` to see major theories
    Type `!psychbiology` to study unit 1
    Type `!psychcognition` to study unit 2
    Type `!psychdevelopment` to study unit 3
    Type `!psychsocial` to study unit 4
    Type `!psychhealth` to study unit 5
    Type `!psychstudyguide` to get access to an exclusive study guide!
    """)
    await asyncio.sleep(1)


@bot.command()
async def psychquizlets(ctx):
    await ctx.send(
        "Here is the full APPSYCH FLASHCARDS https://quizlet.com/user/quizlette83690296/folders/ap-psychology?funnelUUID=86486713-9097-4927-8285-962999385733"
    )


@bot.command()
async def psychtheories(ctx):
    await ctx.send(
        """**Here are the major theories you need to know for AP Psychology**
1. Psychoanalytic Theory (Freud)
2. Behaviorism (Watson, Skinner)
3. Humanistic Theory (Rogers, Maslow)
4. Cognitive Development Theory (Piaget)
5. Social Learning Theory (Bandura)
6. Attachment Theory (Bowlby, Ainsworth)
7. Moral Development Theory (Kohlberg)
8. Trait Theory (Allport, Eysenck, McCrae & Costa)
9. Biological Perspective (Sperry, Gazzaniga)
10. Sociocultural Perspective (Vygotsky)
11. Evolutionary Perspective (Darwin)
12. Drive-Reduction Theory (Hull)
13. Incentive Theory
14. Cognitive Dissonance Theory (Festinger)
15. Two-Factor Theory of Emotion (Schachter-Singer)
""")
    await asyncio.sleep(1)


@bot.command()
async def psychbiology(ctx):
    await ctx.send("""**AP PSYCHOLOGY UNIT 1**
1. **Neurons and Neural Communication:** How neurons transmit signals through electrical impulses and synapses.
2. **Neurotransmitters:** Chemicals (e.g., dopamine, serotonin) that transmit signals between neurons, affecting mood and behavior.
3. **Central and Peripheral Nervous Systems:** CNS (brain and spinal cord) vs. PNS (somatic and autonomic systems controlling voluntary and involuntary actions).
4. **Brain Structures:** Parts of the brain (e.g., amygdala, hippocampus) and their roles in behavior and cognition.
5. **Endocrine System:** Glands (e.g., pituitary, adrenal) that release hormones regulating growth, metabolism, and mood.
6. **Brain Imaging Techniques:** Methods (EEG, MRI, fMRI, PET) used to study brain activity and structure.
7. **Genetics and Behavior:** How genes and heredity influence personality, intelligence, and mental disorders.
8. **Sleep and Dream Theories:** Stages of sleep, REM, and theories about why we dream.
9. **Nature vs. Nurture:** Debate on whether genetics (nature) or environment (nurture) shapes behavior.
10. **Psychoactive Drugs:** Substances that alter brain function, including stimulants, depressants, hallucinogens.
    """)
    await asyncio.sleep(1)


@bot.command()
async def psychcognition(ctx):
    await ctx.send("""**AP PSYCHOLOGY UNIT 2**
    1. **Memory:** Encoding, storage, and retrieval processes; types of memory (sensory, short-term, long-term).
    2. **Forgetting and Memory Distortion:** Decay, interference, repression, and false memories.
    3. **Cognitive Processes:** Problem-solving, decision-making, and creativity.
    4. **Language:** Structure (phonemes, morphemes), language acquisition, and theories (Chomsky, Skinner).
    5. **Thinking and Problem Solving:** Algorithms, heuristics, insight, and obstacles (e.g., functional fixedness).
    6. **Concepts and Prototypes:** How we organize information and form categories.
    7. **Biases and Errors:** Confirmation bias, hindsight bias, and availability heuristic.
    8. **Intelligence and Testing:** IQ, multiple intelligences (Gardner), triarchic theory (Sternberg), emotional intelligence.
    9. **Theories of Intelligence:** Spearman’s g factor, Thurstone’s primary mental abilities.
    10. **Standardization and Norms:** How tests are developed, reliability, and validity.
        """)
    await asyncio.sleep(1)


@bot.command()
async def psychdevelopment(ctx):
    await ctx.send("""**AP PSYCHOLOGY UNIT 3**
    1. **Developmental Theories:** 
       - Piaget’s Stages of Cognitive Development
       - Erikson’s Psychosocial Stages
       - Kohlberg’s Stages of Moral Development
    2. **Prenatal Development:** Stages (germinal, embryonic, fetal) and teratogens.
    3. **Infancy and Childhood:** Attachment theories (Harlow, Ainsworth), parenting styles (Baumrind).
    4. **Adolescence:** Identity formation, social identity, peer influence.
    5. **Adulthood and Aging:** Physical, cognitive, and social changes.
    6. **Classical Conditioning:** Pavlov’s experiments, UCS, UCR, CS, CR.
    7. **Operant Conditioning:** Skinner’s experiments, reinforcement (positive/negative), punishment.
    8. **Social Learning:** Bandura’s Bobo doll experiment, observational learning.
    9. **Cognitive Learning:** Insight (Köhler), latent learning (Tolman), learned helplessness (Seligman).
    10. **Behavioral Theories:** Associative learning, habituation, shaping."""
                   )
    await asyncio.sleep(1)


@bot.command()
async def psychsocial(ctx):
    await ctx.send("""**AP PSYCHOLOGY UNIT 4**
    1. **Social Psychology:**
       - Attribution Theory: Dispositional vs. situational attributions.
       - Fundamental Attribution Error: Overestimating personality traits over situational factors.
       - Attitudes and Actions: How attitudes influence behavior (e.g., cognitive dissonance).
       - Conformity and Obedience: Asch’s conformity experiments, Milgram’s obedience study.
       - Group Behavior: Social facilitation, social loafing, deindividuation.
       - Groupthink and Group Polarization: Decision-making in groups.
       - Prejudice and Discrimination: In-group vs. out-group bias.
       - Altruism and Prosocial Behavior: Helping behavior and factors influencing it.
       - Aggression: Biological, psychological, and social-cultural influences.

    2. **Personality:**
       - Psychoanalytic Theory (Freud): Id, ego, superego, defense mechanisms.
       - Trait Theories: Big Five personality traits (OCEAN).
       - Humanistic Perspectives: Rogers' self-concept, Maslow’s hierarchy of needs.
       - Social-Cognitive Perspective: Bandura’s reciprocal determinism.
       - Personality Assessment: Projective tests (Rorschach, TAT), self-report inventories (MMPI).
       - Locus of Control: Internal vs. external.
       - Self-Efficacy and Self-Esteem: Beliefs about one's own abilities and self-worth.
    """)
    await asyncio.sleep(1)


@bot.command()
async def psychhealth(ctx):
    await ctx.send("""**AP PSYCHOLOGY UNIT 5**
    1. **Stress and Health:** 
       - Stressors: Catastrophes, significant life changes, daily hassles.
       - General Adaptation Syndrome (GAS): Alarm, resistance, exhaustion (Selye).
       - Coping Mechanisms: Problem-focused vs. emotion-focused coping.
       - Health Effects: Psychophysiological illnesses, chronic stress, and immune system suppression.

    2. **Abnormal Psychology:** 
       - Defining Psychological Disorders: Criteria (deviance, distress, dysfunction, danger).
       - DSM-5 Classification: Diagnostic criteria and categories.
       - Anxiety Disorders: Generalized anxiety disorder, panic disorder, phobias.
       - Mood Disorders: Major depressive disorder, bipolar disorder.
       - Schizophrenia: Symptoms (delusions, hallucinations, disorganized speech).
       - Personality Disorders: Antisocial, borderline, narcissistic.
       - Neurodevelopmental Disorders: Autism spectrum disorder, ADHD.

    3. **Therapies and Treatment:**
       - Psychodynamic Therapy: Unconscious conflicts, free association.
       - Cognitive-Behavioral Therapy (CBT): Changing thought patterns.
       - Humanistic Therapy: Client-centered, active listening (Rogers).
       - Biomedical Therapies: Medication (antidepressants, antipsychotics), ECT, psychosurgery.
       - Group and Family Therapy: Social support and communication.

    4. **Health Psychology:** 
       - Biopsychosocial Model: Interaction of biological, psychological, and social factors.
       - Promoting Health: Exercise, nutrition, sleep, and stress management.
       - Positive Psychology: Building resilience and well-being.
        """)
    await asyncio.sleep(1)


@bot.command()
async def psychstudyguide(ctx):
    await ctx.send(
        "**Here is the full APPSYCH STUDY GUIDE** https://www.jackson.stark.k12.oh.us/site/handlers/filedownload.ashx?moduleinstanceid=2468&dataid=13229&FileName=studyguideupdate_docx%20_1_%20_1_.pdf"
    )
    await asyncio.sleep(1)


@bot.command()
async def APPRECALC(ctx):
    await ctx.send("""**AP Precalculus Topics to Study**
**Unit 1**: Polynomial and Rational Functions
Understand how quantities change with each other.
Describe end behavior of functions.
Identify asymptotes and holes in rational function graphs.
Model scenarios using polynomial/rational functions.
Recognize assumptions and limitations of models.
**Unit 2**: Exponential and Logarithmic Functions
Relate geometric sequences and exponential functions.
Model data with exponential functions.
Compose functions and find inverses.
Model scenarios with logarithmic functions.
Validate models using residual plots.
**Unit 3**: Trigonometric and Polar Functions
Link right triangle trigonometry to sine, cosine, tangent.
Model data with sinusoidal functions.
Solve equations using inverse trigonometric functions.
Graph functions in polar coordinates.
Analyze changes in angles/radii in polar graphs.
**Unit 4**: Functions with Parameters, Vectors, and Matrices
Analyze how quantities change in parametric functions.
Graph conic sections with parametric/implicit functions.
Use vectors to describe motion.
Understand transformations with matrices.
Model contextual change with matrices
Type `!precalcformulas` to see important formulas!
Type `!precalcpractice` to get access to practice problems!
Type `!precalctips` to get tips for the exam!
Type `!precalcunit1` to study unit 1
Type `!precalcunit2` to study unit 2
Type `!precalcunit3` to study unit 3
Type `!precalcunit4` to study unit 4
Type `!precalcstudyguide` to get access to an exclusive study guide!
""")
    await asyncio.sleep(1)


@bot.command()
async def precalcformulas(ctx):
    await ctx.send("""**AP Precalculus Formulas** 
    **Unit 1: Polynomial and Rational Functions**  
    - Quadratic Formula: `x = (-b ± √(b² - 4ac)) / 2a`  
    - Rational Zeros: `(factors of constant) / (factors of leading coefficient)`  
    - End Behavior:  
      - Even degree: Same direction  
      - Odd degree: Opposite direction  
    - Horizontal Asymptotes:  
      - Degree num < denom: `y = 0`  
      - Degree num = denom: `y = a/b`  
      - Degree num > denom: No horizontal asymptote  
    **Unit 2: Exponential and Logarithmic Functions**  
    - Exponential Growth/Decay: `A = A₀ * e^(kt)`  
    - Log Properties:  
      - Product: `log_b(xy) = log_b x + log_b y`  
      - Quotient: `log_b(x/y) = log_b x - log_b y`  
      - Power: `log_b(x^n) = n * log_b x`  
    - Change of Base: `log_b a = log a / log b`  
    **Unit 3: Trigonometric and Polar Functions**  
    - Pythagorean Identity: `sin²θ + cos²θ = 1`  
    - Double-Angle Formulas:  
      - `sin(2θ) = 2sinθcosθ`  
      - `cos(2θ) = cos²θ - sin²θ`  
    - Polar to Rectangular:  
      - `x = r * cosθ`  
      - `y = r * sinθ`  
    **Unit 4: Parameters, Vectors, and Matrices**  
    - Vector Magnitude: `||v|| = √(a² + b²)`  
    - Dot Product: `a · b = a₁b₁ + a₂b₂`  
    - Rotation Matrix:  """)

    await asyncio.sleep(1)


@bot.command()
async def precalcpractice(ctx):
    await ctx.send(
        """https://apcentral.collegeboard.org/media/pdf/ap-precalculus-practice-exam-multiple-choice-section.pdf"""
    )
    await asyncio.sleep(1)


@bot.command()
async def precalctips(ctx):
    await ctx.send("""📚 **AP Precalculus Study Tips**  
1. **Understand Core Concepts**  
   Focus on understanding key concepts like functions, transformations, and trigonometry.  

2. **Practice, Practice, Practice**  
   Consistent practice will solidify your understanding.  

3. **Use Visual Aids**  
   Sketch graphs and functions to understand their behaviors better.  

4. **Know Your Trigonometric Identities**  
   Memorize and apply basic trig identities.  

5. **Focus on Word Problems**  
   Practice converting word problems into equations.  

6. **Review Old Tests and Practice AP Questions**  
   Use past AP exam questions to familiarize yourself with the test format.  

7. **Master Graphing**  
   Be able to quickly graph different types of functions.  

8. **Don't Rush Through Homework**  
   Understand each step and avoid rushing.  

9. **Stay Organized**  
   Keep your notes and formulas well-organized.  

10. **Use Online Resources**  
    Use educational websites and videos to reinforce concepts.  

Good luck and happy studying! 💡""")
    await asyncio.sleep(1)


@bot.command()
async def precalcunit1(ctx):
    await ctx.send(
        """**AP Precalculus Unit 1: Polynomial and Rational Functions**
    **Functions and Their Representations:**
    Understanding functions as mathematical models, including function notation, domain, and range. Representing functions graphically, numerically (tables), analytically (equations), and verbally (descriptions).

    **Types of Functions:**
    Linear, quadratic, polynomial, rational, exponential, logarithmic, and piecewise functions. Identifying their characteristics and differences.

   ** Transformations of Functions:**
    Understanding shifts (horizontal and vertical), reflections (across axes), stretches, and compressions. Analyzing how transformations affect the graph of a function.

   ** Operations with Functions:**
    Performing arithmetic operations (addition, subtraction, multiplication, division) and composition of functions. Understanding how combining functions changes their behavior.

    **Inverse Functions:**
    Finding and verifying inverse functions. Analyzing graphical symmetry and algebraic methods to determine inverses.

   ** Modeling Real-World Situations:**
    Using functions to represent practical scenarios, such as population growth, projectile motion, and financial calculations. Applying functions to problem-solving in context.

   ** Key Concepts in Graphing:**
    Identifying key features like intercepts, asymptotes, intervals of increase/decrease, maximums, minimums, and end behavior.

   ** Function Behavior:**
    Analyzing the continuity, limits, and asymptotic behavior of functions. Exploring rates of change and how they relate to real-world phenomena.

   ** Piecewise and Absolute Value Functions:**
    Defining and graphing functions that change behavior over different intervals. Analyzing their structure and how they differ from standard functions.
    
    """)
    await asyncio.sleep(1)


@bot.command()
async def precalcunit2(ctx):
    part_1 = ("""**AP Precalculus Unit 2: Exponential and Logarithmic Functions**
**Rates of Change:**
Understanding average and instantaneous rates of change, including calculating the slope of a secant line and estimating the slope of a tangent line. Applying rates of change to real-world scenarios.

**Linear Functions and Modeling:**
Representing relationships with linear functions, interpreting slope and intercepts, and applying linear models to data. Analyzing direct variation and proportional relationships.

**Exponential and Logarithmic Functions:**
Exploring exponential growth and decay. Understanding logarithms as inverses of exponentials. Applying properties of logarithms to simplify expressions and solve equations.

**Modeling with Exponential Functions:**
Applying exponential models to situations like population growth, radioactive decay, and compound interest. Using logarithmic transformations to linearize data.
""")
    await asyncio.sleep(1)
    await ctx.send(part_1)

    part_2 = ("""**Arithmetic and Geometric Sequences:**
Identifying arithmetic (constant difference) and geometric (constant ratio) sequences. Writing explicit and recursive formulas for sequences and finding specific terms.

**Series and Summation Notation:**
Understanding the sum of finite and infinite series. Using sigma notation to represent sums and applying formulas for arithmetic and geometric series.

**Solving Exponential and Logarithmic Equations:**
Using algebraic techniques and properties of exponents and logarithms to isolate variables and find solutions. Applying logarithms to solve equations involving exponential functions.

**Exponential Models and Regression:**
Using technology to fit exponential models to data. Interpreting parameters of regression equations and evaluating model accuracy.

**Applications in Growth and Decay:**
Applying exponential and logarithmic functions to model scenarios like population growth, investment growth, and cooling/heating processes.

**Graphing Exponential and Logarithmic Functions:**
Understanding the shape, asymptotes, and transformations of exponential and logarithmic graphs. Analyzing how changes to the function’s equation affect the graph’s appearance.
""")
    await asyncio.sleep(1)
    await ctx.send(part_2)


@bot.command()
async def precalcunit3(ctx):
    part_1 = ("""**AP Precalculus Unit 3: Trigonometric and Polar Functions**

**Polynomial Functions:**
Understanding the structure of polynomial functions, including degree, leading coefficient, and end behavior. Exploring how the degree and sign of the leading coefficient affect the graph's shape.

**Zeros and Roots of Polynomials:**
Finding zeros algebraically (factoring, synthetic division) and graphically (x-intercepts). Understanding the multiplicity of roots and its effect on the graph (touching vs. crossing the x-axis).

**Factoring Polynomials:**
Applying techniques such as factoring by grouping, difference of squares, sum/difference of cubes, and the quadratic formula for solving higher-degree equations.

**The Remainder and Factor Theorems:**
Using the Remainder Theorem to evaluate polynomial functions at a given value. Applying the Factor Theorem to determine whether a binomial is a factor of a polynomial.

**Polynomial Division:**
Performing long division and synthetic division to divide polynomials. Using division to simplify expressions and find factors.
""")
    await asyncio.sleep(1)
    await ctx.send(part_1)

    part_2 = ("""**Graphing Polynomial Functions:**
Identifying key features such as x-intercepts, y-intercepts, turning points, and end behavior. Sketching polynomial graphs using zeros and the sign of the leading coefficient.

**Rational Functions:**
Understanding the form of rational functions (ratios of polynomials). Identifying vertical and horizontal asymptotes, holes, and end behavior.

**Solving Rational Equations:**
Clearing denominators to solve equations involving rational expressions. Checking for extraneous solutions.

**Applications of Polynomial and Rational Functions:**
Modeling real-world problems with polynomial and rational functions, including physics applications (motion, projectile paths) and economics (cost, revenue functions).

**Graphing Rational Functions:**
Analyzing asymptotic behavior, intercepts, and the behavior near vertical asymptotes. Graphing by finding the domain, intercepts, asymptotes, and holes.
""")
    await asyncio.sleep(1)
    await ctx.send(part_2)

@bot.command()
async def precalcunit4(ctx):
    part_1 = ("""**AP Precalculus Unit 4: Functions with Parameters, Vectors, and Matrices**

**Trigonometric Functions:**
Understanding the six trigonometric functions (sine, cosine, tangent, cosecant, secant, cotangent) and their relationships. Using the unit circle to define trig functions based on angle measures.

**Radians and Degrees:**
Converting between radians and degrees. Understanding the concept of radians as arc length on the unit circle.

**The Unit Circle:**
Memorizing key angles (0, π/6, π/4, π/3, π/2, etc.) and their corresponding coordinates. Using the unit circle to find trig values for standard angles.

**Graphing Trigonometric Functions:**
Sketching sine, cosine, and tangent functions, including transformations (amplitude, period, phase shift, vertical shift). Understanding the basic shapes and periodic nature of trig graphs.

**Trigonometric Identities:**
Using fundamental identities like the Pythagorean, reciprocal, and quotient identities to simplify expressions. Proving and applying identities in equations.
""")
    await asyncio.sleep(1)
    await ctx.send(part_1)

    part_2 = ("""**Inverse Trigonometric Functions:**
Understanding the restricted domains for the inverse functions of sine, cosine, and tangent. Solving equations involving arcsin, arccos, and arctan.

**Solving Trigonometric Equations:**
Applying algebraic techniques and identities to find solutions within given intervals. Using reference angles and the unit circle to find all solutions.

**Applications of Trigonometry:**
Modeling periodic phenomena (like sound waves or tides) using sine and cosine functions. Applying trigonometry to solve problems involving angles of elevation and depression.

**Law of Sines and Law of Cosines:**
Solving oblique triangles (non-right triangles) using these laws. Applying them to find missing sides and angles in real-world problems.

**Polar Coordinates and Complex Numbers:**
Representing points in polar form (r, θ) and converting between polar and rectangular coordinates. Understanding how complex numbers can be represented as vectors in the plane.
""")
    await asyncio.sleep(1)
    await ctx.send(part_2)


@bot.command()
async def precalcstudyguide(ctx):
    await ctx.send(
        "**Here is the full APPRECALC STUDY GUIDE** https://uploads-ssl.webflow.com/605fe570e5454a357d1e1811/6062b54315cd84377fe3c07e_SS-Precalc-1.pdf"
    )
    await asyncio.sleep(1)

@bot.command()
async def APLANG(ctx):
    await ctx.send("""**AP Language and Composition Topics to Study**
1. **Rhetorical Situation: Reading**:  Explain how writers’ choices reflect the components of the rhetorical situation.
2. **Rhetorical Situation: Writing**:  Analyze how the rhetorical situation influences the writer’s choices.
3. **Claims and Evidence: Reading**:  Analyze the relationship between claims and evidence in texts.
4. **Claims and Evidence: Writing**:  Support claims with evidence and reasoning.
5. **Reasoning and Organization: Reading**:  Analyze the organization of texts and how it supports the argument.
6. **Reasoning and Organization: Writing**:  Organize writing to support the argument.
7. **Style and Tone: Reading**:  Analyze the style and tone of texts.
8. **Style and Tone: Writing**:  Use style and tone to enhance the argument.

Type `!langvocab` to see important formulas!
Type `!langpractice` to get access to practice problems!
Type `!langtips` to get tips for the exam!
Type `!langstudyguide` to get access to an exclusive study guide!
""")

@bot.command()
async def langvocab(ctx):
    part_1 = """**AP LANG VOCAB**
1. Allegory - A story with a hidden meaning.
2. Alliteration - Repetition of consonant sounds at the beginning of words.
3. Allusion - A reference to another work or event.
4. Analogy - A comparison between two things for clarification.
5. Anaphora - Repetition of a word or phrase at the beginning of clauses.
6. Anecdote - A short, personal story.
7. Antithesis - The juxtaposition of contrasting ideas.
8. Aphorism - A concise statement of a general truth.
9. Apostrophe - Addressing an absent or imaginary person.
10. Archetype - A typical example of something.
11. Assonance - Repetition of vowel sounds.
12. Asyndeton - Omission of conjunctions.
13. Chiasmus - A reversal in the order of words in two parallel phrases.
14. Colloquialism - Informal words or expressions.
15. Connotation - The implied meaning of a word.
16. Denotation - The literal meaning of a word.
17. Diction - Word choice.
18. Euphemism - A mild or indirect expression replacing a harsher one.
19. Hyperbole - Exaggeration for effect.
20. Imagery - Language that appeals to the senses.
    """
    await ctx.send(part_1)
    part_2 = """
21. Irony - A contrast between expectation and reality.
22. Juxtaposition - Placing two elements close together for contrast.
23. Metaphor - A figure of speech comparing two unlike things without using 'like' or 'as'.
24. Metonymy - Substituting a name with something closely related.
25. Onomatopoeia - A word that imitates a sound.
26. Oxymoron - Combining contradictory terms.
27. Paradox - A statement that seems contradictory but reveals a truth.
28. Parallelism - Similar structure in a pair or series of words or phrases.
29. Personification - Giving human traits to non-human things.
30. Polysyndeton - The use of many conjunctions.
31. Pun - A play on words.
32. Satire - Using humor to criticize.
33. Simile - A comparison using 'like' or 'as'.
34. Symbolism - Using symbols to represent ideas.
35. Synecdoche - A part is made to represent the whole.
36. Syntax - The arrangement of words and phrases.
37. Theme - The underlying message of a text.
38. Tone - The author's attitude toward the subject.
39. Understatement - Making something seem less important than it is.
40. Zeugma - Using a word to apply to multiple parts of a sentence."""
    await ctx.send(part_2)
@bot.command ()   
async def langpractice(ctx):
    await ctx.send("""**AP LANG PRACTICE**
1. **Reading Practice**: Read a variety of texts and analyze their rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
2. **Writing Practice**: Write essays that demonstrate your understanding of the rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
3. **Vocabulary Practice**: Learn and use a variety of rhetorical devices and vocabulary terms.
4. **Grammar Practice**: Practice using correct grammar and punctuation.
5. **Style and Tone Practice**: Practice using style and tone to enhance your writing.
6. **AP Practice Tests**: Take AP practice tests to familiarize yourself with the format and types of questions on the AP exam.
7. **Peer Review**: Have a friend or teacher review your writing and provide feedback.
8. **Online Resources**: Use online resources such as Khan Academy, Quizlet, and AP Classroom to practice and review.
9. **Study Groups**: Join or form a study group to practice and review with others.
10. **Flashcards**: Use flashcards to memorize vocabulary and rhetorical devices.
11. **AP Classroom**: Use AP Classroom to access resources, practice problems, and quizzes. https://apcentral.collegeboard.org/courses/ap-english-language-and-composition/exam/past-exam-questions
""")
    await asyncio.sleep(1)

@bot.command()
async def langtips(ctx):
    await ctx.send("""**AP LANG TIPS**
    1. **Read Widely**: Read a variety of texts to improve your reading comprehension and vocabulary.
    2. **Write Regularly**: Write essays regularly to improve your writing skills.
    3. **Use Rhetorical Devices**: Learn and use a variety of rhetorical devices to enhance your writing.
    4. **Practice Grammar**: Practice using correct grammar and punctuation.
    5. **Use Style and Tone**: Use style and tone to enhance your writing.
    6. **Take AP Practice Tests**: Take AP practice tests to familiarize yourself with the format and types of questions on the AP exam.
    7. **Join a Study Group**: Join or form a study group to practice and review with others.
    8. **Use Flashcards**: Use flashcards to memorize vocabulary and rhetorical devices.
    9. **Use Online Resources**: Use online resources such as Khan Academy, Quizlet, and AP Classroom to practice and review.
    10. **Peer Review**: Have a friend or teacher review your writing and provide feedback.
    """)
    await asyncio.sleep(1)

@bot.command()
async def langstudyguide(ctx):
    await ctx.send("""**AP LANG STUDY GUIDE**
    1. **Reading**: Read a variety of texts and analyze their rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
    2. **Writing**: Write essays that demonstrate your understanding of the rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
    3. **Vocabulary**: Learn and use a variety of rhetorical devices and vocabulary terms.
    4. **Grammar**: Practice using correct grammar and punctuation.
    5. **Style and Tone**: Practice using style and tone to enhance your writing.
    6. **AP Practice Tests**: Take AP practice tests to familiarize yourself with the format and types of questions on the AP exam.
    7. **Peer Review**: Have a friend or teacher review your writing and provide feedback.
    8. **Online Resources**: Use online resources such as Khan Academy, Quizlet, and AP Classroom to practice and review.
    9. **Study Groups**: Join or form a study group to practice and review with others.
    10. **Flashcards**: Use flashcards to memorize vocabulary and rhetorical devices.
    11. **AP Classroom**: Use AP Classroom to access resources, practice problems, and quizzes. https://apcentral.collegeboard.org/courses/ap-english-language-and-composition/exam/past-exam-questions
    """)
    await asyncio.sleep(1)

@bot.command()
async def APLIT(ctx):
    await ctx.send("""**AP Literature and Composition Topics to Study**

**Unit 1: Short Fiction I**
Learn critical reading skills to interpret and analyze prose.

**Unit 2: Poetry I**
Explore poetry analysis across a variety of poems.

**Unit 3: Longer Fiction or Drama I**
Analyze character development and interaction in longer works.

**Unit 4: Short Fiction II**
Delve deeper into character roles, conflict, and narrator perspective.

**Unit 5: Poetry II**
Study poetry forms and how structure and figurative language affect meaning.

**Unit 6: Longer Fiction or Drama II**
Track literary techniques and character changes over longer works.

**Unit 7: Short Fiction III**
Examine fiction’s commentary on society and the author’s context.

**Unit 8: Poetry III**
Develop interpretation by analyzing contrasts, ambiguity, and technique.

**Unit 9: Longer Fiction or Drama III**
Build nuanced analysis of complex longer narratives using prior techniques.

Type `!litvocab` for vocabulary lists!  
Type `!litpractice` for practice questions!  
Type `!littips` for exam tips!  
Type `!litstudyguide` for an exclusive study guide!
""")
    await asyncio.sleep(1)

@bot.command()
async def litvocab(ctx):
    part_1 = """
**AP Literature Vocabulary Part 1**
1. **Allusion** – A reference to another text, event, or figure.
2. **Ambiguity** – Multiple meanings or interpretations.
3. **Analogy** – Comparison to explain or clarify.
4. **Antagonist** – Character opposing the protagonist.
5. **Apostrophe** – Direct address to an absent or imaginary person.
6. **Archetype** – A universal symbol or pattern.
7. **Bildungsroman** – A coming-of-age story.
8. **Caesura** – A pause or break within a line of poetry.
9. **Catharsis** – Emotional release experienced by the audience.
10. **Characterization** – The process of developing a character.
"""
    part_2 = """
**AP Literature Vocabulary Part 2**
11. **Denotation** – Literal dictionary meaning of a word.
12. **Denouement** – The resolution or conclusion of a story.
13. **Diction** – Choice of words and style of expression.
14. **Dramatic Irony** – When the audience knows something characters don’t.
15. **Enjambment** – Continuation of a sentence without pause beyond a line of poetry.
16. **Epiphany** – Sudden insight or realization.
17. **Epilogue** – Final section of a literary work.
18. **Euphemism** – Mild or indirect word substituted for something harsh.
19. **Foil** – Character who contrasts with another to highlight qualities.
20. **Foreshadowing** – Hinting at future events.
"""
    part_3 = """
**AP Literature Vocabulary Part 3**
21. **Hyperbole** – Exaggeration for effect.
22. **Imagery** – Descriptive language appealing to the senses.
23. **Irony** – A contrast between expectation and reality.
24. **Metaphor** – Direct comparison without “like” or “as.”
25. **Motif** – Repeated symbol or idea.
26. **Narrator** – The voice telling the story.
27. **Onomatopoeia** – Words that imitate sounds.
28. **Oxymoron** – Contradictory terms appear together.
29. **Paradox** – A statement that seems contradictory but reveals truth.
30. **Personification** – Giving human qualities to non-human things.
"""

    await ctx.send(part_1)
    await ctx.send(part_2)
    await ctx.send(part_3)

@bot.command()
async def litpractice(ctx):
    await ctx.send("""**AP Literature Practice Questions**
1. **Reading Practice**: Read a variety of texts and analyze their rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
2. **Writing Practice**: Write essays that demonstrate your understanding of the rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
3. **Vocabulary Practice**: Learn and use a variety of rhetorical devices and vocabulary terms.
4. **Grammar Practice**: Practice using correct grammar and punctuation.
5. **Style and Tone Practice**: Practice using style and tone to enhance your writing.
6. **AP Practice Tests**: Take AP practice tests to familiarize yourself with the format and types of questions on the AP exam.
7. **Peer Review**: Have a friend or teacher review your writing and provide feedback.
8. **Online Resources**: Use online resources such as Khan Academy, Quizlet, and AP Classroom to practice and review.
9. **Study Groups**: Join or form a study group to practice and review with others.
10. **Flashcards**: Use flashcards to memorize vocabulary and rhetorical devices.
11. **AP Classroom**: Use AP Classroom to access resources, practice problems, and quizzes. https://apcentral.collegeboard.org/courses/ap-english-literature-and-composition/exam/past-exam-questions
""")
    await asyncio.sleep(1)

@bot.command()
async def littips(ctx):
    await ctx.send("""**AP Literature Exam Tips**
1. **Read Widely**: Read a variety of texts to improve your reading comprehension and vocabulary.
2. **Write Regularly**: Write essays regularly to improve your writing skills.
3. **Use Rhetorical Devices**: Learn and use a variety of rhetorical devices to enhance your writing.
4. **Practice Grammar**: Practice using correct grammar and punctuation.
5. **Use Style and Tone**: Use style and tone to enhance your writing.
6. **Take AP Practice Tests**: Take AP practice tests to familiarize yourself with the format and types of questions on the AP exam.
7. **Join a Study Group**: Join or form a study group to practice and review with others.
8. **Use Flashcards**: Use flashcards to memorize vocabulary and rhetorical devices.
9. **Use Online Resources**: Use online resources such as Khan Academy, Quizlet, and AP Classroom to practice and review.
10. **Peer Review**: Have a friend or teacher review your writing and provide feedback.
""")
    await asyncio.sleep(1)

@bot.command()
async def litstudyguide(ctx):
    await ctx.send("""**AP Literature Study Guide**
1. **Reading**: Read a variety of texts and analyze their rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
2. **Writing**: Write essays that demonstrate your understanding of the rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
3. **Vocabulary**: Learn and use a variety of rhetorical devices and vocabulary terms.
4. **Grammar**: Practice using correct grammar and punctuation.
5. **Style and Tone**: Practice using style and tone to enhance your writing.
6. **AP Practice Tests**: Take AP practice tests to familiarize yourself with the format and types of questions on the AP exam.
7. **Peer Review**: Have a friend or teacher review your writing and provide feedback.
8. **Online Resources**: Use online resources such as Khan Academy, Quizlet, and AP Classroom to practice and review.
9. **Study Groups**: Join or form a study group to practice and review with others.
10. **Flashcards**: Use flashcards to memorize vocabulary and rhetorical devices.
11. **AP Classroom**: Use AP Classroom to access resources, practice problems, and quizzes. https://apcentral.collegeboard.org/courses/ap-english-literature-and-composition/exam/past-exam-questions
""")
    await asyncio.sleep(1)

@bot.command()
async def APBIO(ctx):
    await ctx.send("""**AP Biology Topics to Study**
    **Unit 1: Chemistry of Life**  
    Learn about water’s role as the basis of life and functions of macromolecules like lipids and proteins.

    **Unit 2: Cell Structure and Function**  
    Study the makeup of cells and the fundamentals of evolution.

    **Unit 3: Cellular Energetics**  
    Explore how cells interact with their environment and how fundamental biological processes work at the cellular level.

    **Unit 4: Cell Communication and Cell Cycle**  
    Learn how cells grow, reproduce, and communicate.

    **Unit 5: Heredity**  
    Understand how traits are passed down from one generation to the next.

    **Unit 6: Gene Expression and Regulation**  
    Study how hereditary information is passed from parent to offspring and how traits are expressed.

    **Unit 7: Natural Selection**  
    Learn about Darwin’s theory, natural selection, and evolution.

    **Unit 8: Ecology**  
    Explore biological concepts at organism and population levels and analyze ecosystem interactions.

    Type `!biounit1` to study unit 1
    Type `!biounit2` to study unit 2
    Type `!biounit3` to study unit 3
    Type `!biounit4` to study unit 4
    Type `!biounit5` to study unit 5
    Type `!biounit6` to study unit 6
    Type `!biounit7` to study unit 7
    Type `!biounit8` to study unit 8
    Type `biopractice ` to get access to practice problems!
    Type `biostudyguide` to get access to an exclusive study guide!
    """)
    await asyncio.sleep(1)

@bot.command()
async def biounit1(ctx):
    await ctx.send("""**AP Biology Unit 1: Chemistry of Life**
    1. **Water Properties:** Cohesion, adhesion, high specific heat, solvent abilities, and polarity.
    2. **Macromolecules:** 
       - **Carbohydrates:** Energy storage and structural components.
       - **Lipids:** Fats, oils, membranes, and energy storage.
       - **Proteins:** Enzymes, structure, transport, and signaling.
       - **Nucleic Acids:** DNA and RNA for genetic information.
    3. **Enzymes:** Biological catalysts, activation energy, and factors affecting enzyme activity (temperature, pH, inhibitors).
    4. **pH and Buffers:** Acidic, basic, and neutral solutions; how buffers maintain homeostasis.
    5. **Carbon’s Role:** Carbon’s ability to form diverse molecules due to four valence electrons.
    6. **Functional Groups:** Key groups like hydroxyl, carboxyl, amino, phosphate, and their roles in molecules.
    """)
    await asyncio.sleep(1)

@bot.command()
async def biounit2(ctx):
    await ctx.send("""**AP Biology Unit 2: Cell Structure and Function**
    1. **Cell Theory:** All living things are made of cells; cells are the basic units of life; all cells come from pre-existing cells.
    2. **Prokaryotic vs. Eukaryotic Cells:** Differences in structure and complexity.
    3. **Cell Organelles and Their Functions:** 
       - Nucleus, ribosomes, endoplasmic reticulum (rough and smooth), Golgi apparatus.
       - Mitochondria and chloroplasts (energy conversion).
       - Lysosomes and peroxisomes (waste breakdown).
       - Cytoskeleton (structure and movement).
    4. **Plasma Membrane:** Phospholipid bilayer, selective permeability, fluid mosaic model.
    5. **Transport Mechanisms:** Passive transport (diffusion, osmosis, facilitated diffusion), active transport, endocytosis, exocytosis.
    6. **Cell Communication:** Signal transduction pathways and receptor types.
    7. **Cell Size and Surface Area to Volume Ratio:** Limits on cell size for efficient transport.
    8. **Evolution of Cells:** Endosymbiotic theory and evidence supporting mitochondria and chloroplast origins.
    """)
    await asyncio.sleep(1)

@bot.command()
async def biounit3(ctx):
    await ctx.send("""**AP Biology Unit 3: Cellular Energetics**
    1. **Metabolism:** The sum of all chemical reactions in a cell, including catabolic and anabolic pathways.
    2. **Enzymes:** Biological catalysts that speed up reactions, including factors affecting enzyme activity (temperature, pH, inhibitors).
    3. **ATP:** The main energy currency of the cell.
    4. **Cellular Respiration:** Process by which cells convert glucose and oxygen into ATP, including glycolysis, Krebs cycle, and oxidative phosphorylation.
    5. **Photosynthesis:** Process by which plants convert light energy into chemical energy, including light reactions and the Calvin cycle.
    6. **Energy Transfer:** Redox reactions and electron transport chains.
    7. **Anaerobic Respiration and Fermentation:** Alternative pathways for energy production without oxygen.
    8. **Coupled Reactions:** Using energy released from exergonic reactions to drive endergonic reactions.
    """)
    await asyncio.sleep(1)

@bot.command()
async def biounit4(ctx):
    await ctx.send("""**AP Biology Unit 4: Cell Communication and Cell Cycle**
    1. **Cell Communication:** Signal transduction pathways, receptors, and second messengers.
    2. **Cell Cycle:** Phases (G1, S, G2, M), checkpoints, and control mechanisms.
    3. **Mitosis:** Process of nuclear division, including prophase, prometaphase, metaphase, anaphase, and telophase.
    4. **Cytokinesis:** Division of the cytoplasm in animal cells.
    5. **Meiosis:** Process of genetic recombination and reduction in chromosome number, including meiosis I and meiosis II.
    6. **Asexual Reproduction:** Processes like binary fission, budding, and fragmentation.
    7. **Sexual Reproduction:** Processes involving gamete formation and fertilization.
    8. **Genetic Variation:** Sources of variation (mutation, crossing over, independent assortment).
    """)
    await asyncio.sleep(1)

@bot.command()
async def biounit5(ctx):
    await ctx.send("""**AP Biology Unit 5: Heredity**
    1. **Mendelian Genetics:** Laws of segregation and independent assortment, Punnett squares, and genetic ratios.
    2. **Chromosomes:** Structure, function, and role in heredity.
    3. **Meiosis:** Process of genetic recombination and reduction in chromosome number.
    4. **Genetic Mutations:** Types (point, frameshift, chromosomal), effects, and mechanisms.
    5. **Genetic Recombination:** Crossing over and its role in genetic variation.
    6. **Polygenic Inheritance:** Multiple genes influencing a trait.
    7. **Epigenetics:** Environmental influences on gene expression.
    8. **Genetic Disorders:** Examples like cystic fibrosis, sickle cell anemia, and Down syndrome.
    """)

@bot.command()
async def biounit6(ctx):
    await ctx.send("""**AP Biology Unit 6: Gene Expression and Regulation**
    1. **Gene Expression:** Transcription and translation processes.
    2. **Gene Regulation:** Mechanisms controlling gene expression (promoters, enhancers, silencers, repressors).
    3. **RNA Processing:** Splicing, polyadenylation, and capping.
    4. **Gene Mutations:** Effects on gene expression and protein function.
    5. **Gene Expression in Prokaryotes:** Differences in gene regulation between prokaryotes and eukaryotes.
    6. **Gene Expression in Eukaryotes:** Eukaryotic gene structure and regulation.
    7. **Gene Expression in Development:** Role of gene regulation in development and differentiation.
    8. **Gene Expression in Disease:** Genetic disorders and their molecular bases.
    """)
    await asyncio.sleep(1)

@bot.command()
async def biounit7(ctx):
    await ctx.send("""**AP Biology Unit 7: Natural Selection**
    1. **Evolution:** Process of change in a population over time.
    2. **Natural Selection:** Mechanism by which populations adapt to their environment.
    3. **Artificial Selection:** Human-driven selection of desirable traits.
    4. **Hardy-Weinberg Principle:** Factors affecting genetic equilibrium.
    5. **Speciation:** Process of formation of new species.
    6. **Phylogenetics:** Study of evolutionary relationships.
    7. **Homology and Analogy:** Similarities and differences in structures.
    8. **Convergent and Divergent Evolution:** Adaptive changes in different lineages.
    """)
    await asyncio.sleep(1)

@bot.command()
async def biounit8(ctx):
    await ctx.send("""**AP Biology Unit 8: Ecology**
    1. **Population Ecology:** Factors affecting population size and distribution.
    2. **Community Ecology:** Interactions between species in an ecosystem.
    3. **Ecosystem Ecology:** Energy flow and nutrient cycling.
    4. **Biodiversity:** Importance and threats to biodiversity.
    5. **Succession:** Process of ecological change over time.
    6. **Human Impact on Ecosystems:** Environmental issues and conservation efforts.
    7. **Biogeochemical Cycles:** Carbon, nitrogen, phosphorus, and sulfur cycles.
    8. **Global Change:** Climate change, ocean acidification, and biodiversity loss.
    """)

@bot.command()
async def biopractice(ctx):
    await ctx.send("""**AP Biology Practice Questions**
    1. **Reading Practice**: Read a variety of texts and analyze their rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
    2. **Writing Practice**: Write essays that demonstrate your understanding of the rhetorical situation, claims and evidence, reasoning and organization, and style and tone.
    3. **Vocabulary Practice**: Learn and use a variety of rhetorical devices and vocabulary terms.
    4. **Grammar Practice**: Practice using correct grammar and punctuation.
    5. **Style and Tone Practice**: Practice using style and tone to enhance your writing.
    6. **AP Practice Tests**: Take AP practice tests to familiarize yourself with the format and types of questions on the AP exam.
    7. **Peer Review**: Have a friend or teacher review your writing and provide feedback.
    8. **Online Resources**: Use online resources such as Khan Academy, Quizlet, and AP Classroom to practice and review.
    9. **Study Groups**: Join or form a study group to practice and review with others.
    10. **Flashcards**: Use flashcards to memorize vocabulary and rhetorical devices.
    11. **AP Classroom**: Use AP Classroom to access resources, practice problems, and quizzes. https://apcentral.collegeboard.org/courses/ap-biology/exam/past-exam-questions
    """)
    await asyncio.sleep(1)

@bot.command()
async def biostudyguide(ctx):
    await ctx.send("""**AP Biology Study Guide**
   https://support.ebsco.com/LEX/AP-Biology-Study-Guide.pdf
   """)

@bot.command()
async def APCHEM(ctx):
    await ctx.send("""**AP Chemistry Topics to Study**
    1. **Atomic Structure and Properties:** Learn about the composition of atoms and ways scientists measure and categorize these building blocks of matter.
    2. **Compound Structure and Properties:** Discover the range of chemical bonds and how their structure can affect the properties of the molecules created.
    3. **Properties of Substances and Mixtures:** Explore how atoms come together to create solids, liquids, and gases, and how forces between particles govern the properties of everything around you.
    4. **Chemical Reactions:** Differentiate physical and chemical processes, and learn to measure and express chemical reactions via chemical equations.
    5. **Kinetics:** Explore various methods to observe changes during a chemical reaction, factors influencing reaction rate, and the relation to elementary reactions.
    6. **Thermochemistry:** Learn about energy changes in chemical reactions and how energy transfer can change a substance’s physical properties.
    7. **Equilibrium:** Chart how chemical reactions change over time, what causes substances to reach equilibrium, and how systems react when equilibrium is disturbed.
    8. **Acids and Bases:** Learn more about pH, the qualities and properties of acids and bases, and their interactions in chemical reactions.
    9. **Thermodynamics and Electrochemistry:** Understand “thermodynamic favorability” for reactions, examining how likely they are to occur given energy changes.

   Type `!chemunit1` to study unit 1
   Type `!chemunit2` to study unit 2
   Type `!chemunit3` to study unit 3
   Type `!chemunit4` to study unit 4
   Type `!chemunit5` to study unit 5
   Type `!chemunit6` to study unit 6
   Type `!chemunit7` to study unit 7
   Type `!chemunit8` to study unit 8
   Type `!chemunit9` to study unit 9
   Type `chempractice ` to get access to practice problems!
   Type `chemstudyguide` to get access to an exclusive study guide!
    """)
    await asyncio.sleep(1)

@bot.command()
async def chemunit1(ctx):
    await ctx.send("""**AP Chemistry Unit 1: Atomic Structure and Properties**
    1. **Atomic Structure:** Electron configuration, periodic trends, and the periodic table.
    2. **Periodic Trends:** Electron affinity, ionization energy, atomic radius, and electronegativity.
    3. **Ionic Bonding:** Formation of ions, lattice energy, and properties of ionic compounds.
    4. **Covalent Bonding:** Polar and nonpolar covalent bonds, bond polarity, and molecular geometry.
    5. **Intermolecular Forces:** Dipole-dipole, hydrogen bonding, and London dispersion forces.
    6. **Molecular Geometry:** VSEPR theory and shapes of molecules.
    7. **Nomenclature:** IUPAC naming conventions for organic compounds.
    8. **Chemical Formulas:** Balancing chemical equations and stoichiometry.
    """)
    await asyncio.sleep(1)

@bot.command()
async def chemunit2(ctx):
    await ctx.send("""**AP Chemistry Unit 2: Compound Structure and Properties**
    1. **Molecular Structure:** Lewis structures, resonance, and formal charge.
    2. **Hybridization:** sp, sp², sp³, and d-orbital hybridization.
    3. **Molecular Polarity:** Dipole moment and polarity of molecules.
    4. **Acid-Base Theories:** Arrhenius, Brønsted-Lowry, and Lewis acid-base theories.
    5. **Nuclear Chemistry:** Radioactive decay, half-life, and types of radiation.
    6. **Organic Chemistry:** Functional groups, isomerism, and reactions of organic compounds.
    7. **Chemical Bonding:** Ionic, covalent, and metallic bonding.
    8. **Chemical Reactions:** Types of reactions (synthesis, decomposition, single-displacement, double-displacement).
    """)
    await asyncio.sleep(1)

@bot.command()
async def chemunit3(ctx):
    await ctx.send("""**AP Chemistry Unit 3: Properties of Substances and Mixtures**
    1. **States of Matter:** Solid, liquid, gas, and plasma states.
    2. **Phase Changes:** Melting, freezing, boiling, and condensation.
    3. **Intermolecular Forces:** Dipole-dipole, hydrogen bonding, and London dispersion forces.
    4. **Colligative Properties:** Boiling point elevation, freezing point depression, and vapor pressure.
    5. **Solutions:** Concentration, molarity, molality, and solubility.
    6. **Solubility Rules:** Factors affecting solubility and solubility rules.
    7. **Electrolytes:** Strong and weak electrolytes, conductivity, and acid-base indicators.
    8. **Chemical Equilibrium:** Le Chatelier’s principle and equilibrium constants.
    """)
    await asyncio.sleep(1)

@bot.command()
async def chemunit4(ctx):
    await ctx.send("""**AP Chemistry Unit 4: Chemical Reactions**
    1. **Stoichiometry:** Balancing chemical equations and calculating amounts of reactants and products.
    2. **Types of Reactions:** Synthesis, decomposition, single-displacement, and double-displacement reactions.
    3. **Acid-Base Reactions:** Neutralization reactions and pH calculations.
    4. **Redox Reactions:** Oxidation states, half-reactions, and balancing redox equations.
    5. **Electrochemistry:** Galvanic cells, electrolytic cells, and Faraday’s laws.
    6. **Thermochemistry:** Enthalpy, heat of reaction, and Hess’s law.
    7. **Kinetics:** Reaction rates, factors affecting reaction rates, and reaction mechanisms.
    8. **Catalysis:** Homogeneous and heterogeneous catalysis, enzyme catalysis, and catalysis in industry.
    """)
    await asyncio.sleep(1)

@bot.command()
async def chemunit5(ctx):
    await ctx.send("""**AP Chemistry Unit 5: Kinetics**
    1. **Reaction Rates:** Factors affecting reaction rates (temperature, concentration, catalyst).
    2. **Rate Laws:** Rate expressions and rate constants.
    3. **Integrated Rate Laws:** Calculating reaction rates and time.
    4. **Collision Theory:** Activation energy, collision frequency, and reaction rate.
    5. **Transition State Theory:** Transition state, activation energy, and reaction rate.
    6. **Catalysis:** Homogeneous and heterogeneous catalysis, enzyme catalysis, and catalysis in industry.
    7. **Reaction Mechanisms:** Elementary reactions and reaction pathways.
    8. **Photochemistry:** Photochemical reactions and photochemical smog.
    """)
    await asyncio.sleep(1)

@bot.command()
async def chemunit6(ctx):
    await ctx.send("""**AP Chemistry Unit 6: Thermochemistry**
    1. **Enthalpy:** Heat of reaction, enthalpy change, and Hess’s law.
    2. **Entropy:** Disorder and entropy, entropy change, and Gibbs free energy.
    3. **Gibbs Free Energy:** Spontaneity of reactions and equilibrium constants.
    4. **Thermodynamic Cycles:** Carnot cycle, efficiency, and entropy.
    5. **Electrochemistry:** Galvanic cells, electrolytic cells, and Faraday’s laws.
    6. **Acid-Base Equilibria:** pH calculations and buffer solutions.
    7. **Solubility Equilibria:** Solubility product constants and solubility rules.
    8. **Complex Ion Equilibria:** Formation constants and stability of complex ions.
    """)
    await asyncio.sleep(1)

@bot.command()
async def chemunit7(ctx):
    await ctx.send("""**AP Chemistry Unit 7: Equilibrium**
    1. **Chemical Equilibrium:** Dynamic equilibrium, equilibrium constants, and Le Chatelier’s principle.
    2. **Haber Process:** Synthesis of ammonia and factors affecting equilibrium.
    3. **Acid-Base Equilibria:** pH calculations and buffer solutions.
    4. **Solubility Equilibria:** Solubility product constants and solubility rules.
    5. **Complex Ion Equilibria:** Formation constants and stability of complex ions.
    6. **Le Chatelier’s Principle:** Shifting equilibrium in response to changes in concentration, temperature, and pressure.
    7. **Equilibrium Constants:** Calculating equilibrium constants and predicting the direction of reactions.
    8. **Ionic Equilibria:** Solubility product constants and solubility rules.
    """)
    await asyncio.sleep(1)

@bot.command()
async def chemunit8(ctx):
    await ctx.send("""**AP Chemistry Unit 8: Acids and Bases**
    1. **Acid-Base Theories:** Arrhenius, Brønsted-Lowry, and Lewis acid-base theories.
    2. **pH and pOH:** Calculating pH and pOH, and buffer solutions.
    3. **Acid-Base Equilibria:** pH calculations and buffer solutions.
    4. **Solubility Equilibria:** Solubility product constants and solubility rules.
    5. **Complex Ion Equilibria:** Formation constants and stability of complex ions.
    6. **Acid-Base Indicators:** pH indicators and their use in titrations.
    7. **Titrations:** Acid-base titrations and stoichiometry.
    8. **Acid-Base Properties:** Strength of acids and bases, and their properties.
    """)
    await asyncio.sleep(1)
    
    @bot.command()
    async def chemunit9(ctx):
        await ctx.send("""**AP Chemistry Unit 9: Thermodynamics and Electrochemistry**
        1. **Thermodynamics:** Enthalpy, entropy, and Gibbs free energy.
        2. **Spontaneity:** Spontaneous and nonspontaneous reactions.
        3. **Gibbs Free Energy:** Calculating Gibbs free energy and predicting the direction of reactions.
        4. **Electrochemistry:** Galvanic cells, electrolytic cells, and Faraday’s laws.
        5. **Electrode Potentials:** Standard electrode potentials and cell potentials.
        6. **Redox Reactions:** Oxidation states, half-reactions, and balancing redox equations.
        7. **Electrolysis:** Electrolytic cells and Faraday’s laws.
        8. **Batteries and Fuel Cells:** Types of batteries and fuel cells, and their applications.
        """)
        await asyncio.sleep(1)

    @bot.command()
    async def chempractice(ctx):
        await ctx.send("""**AP Chemistry Practice Questions**
        1. **Atomic Structure:**  
           - What is the electron configuration of a calcium atom?  
           - Explain the difference between atomic number and mass number.  

        2. **Compound Structure:**  
           - How do ionic and covalent bonds differ in terms of electron sharing?  
           - Draw the Lewis structure for H2O.  

        3. **Properties of Substances and Mixtures:**  
           - What intermolecular forces are present in liquid water?  
           - Define a homogeneous mixture and give two examples.  

        4. **Chemical Reactions:**  
           - Balance the chemical equation: C3H8 + O2 → CO2 + H2O.  
           - What is the molar mass of NaCl?  

        5. **Kinetics:**  
           - How does temperature affect the rate of a chemical reaction?  
           - What is the rate law for the reaction A + B → C if the reaction is first-order with respect to both A and B?  

        6. **Thermochemistry:**  
           - Define enthalpy and its significance in chemical reactions.  
           - How can you determine whether a reaction is endothermic or exothermic?  

        7. **Equilibrium:**  
           - What is Le Chatelier’s principle?  
           - Calculate the equilibrium constant (Kc) for the reaction: N2 + 3H2 ⇌ 2NH3.  

        8. **Acids and Bases:**  
           - What is the pH of a 0.01 M HCl solution?  
           - Define a buffer and explain how it works.  

        9. **Thermodynamics and Electrochemistry:**  
           - What does Gibbs free energy indicate about a chemical reaction?  
           - What is the purpose of a salt bridge in a galvanic cell?  """)
        await asyncio.sleep(1)



@bot.command()
async def chemstudyguide(ctx):
        await ctx.send("""**AP Chemistry Study Guide**
        https://support.ebsco.com/LEX/AP-Chemistry_Study-Guide.pdf
        """)
        await asyncio.sleep(1)

@bot.command()
async def APPHYSICS1(ctx):
    await ctx.send("""**AP Physics Topics to Study**
    1. **Kinematics:**  
       - Study of motion, including displacement, velocity, acceleration, and equations of motion.  
    

    2. **Force and Translational Dynamics:**  
       - Newton’s laws of motion.  
       - Free-body diagrams and net force calculations.  
     force.  

    3. **Work, Energy, and Power:**  
       - Work-energy theorem and conservation of energy.  
       - Kinetic and potential energy.  
       - Power calculations and mechanical advantage.  

    4. **Linear Momentum:**  
       - Impulse-momentum theorem and conservation of momentum.  
       - Elastic and inelastic collisions.  
       - Center of mass and motion of a system.  

    5. **Torque and Rotational Dynamics:**  
       - Rotational motion, angular velocity, and angular acceleration.  
       - Torque, rotational inertia, and Newton’s second law for rotation.  
       - Rotational kinetic energy and conservation of angular momentum.  

    6. **Energy and Momentum of Rotating Systems:**  
       - Rotational kinetic energy vs. linear kinetic energy.  
       - Angular momentum and its conservation.  
       

    7. **Oscillations:**  
       - Simple harmonic motion (SHM), including springs and pendulums.  
       - Energy in oscillating systems and damping.  
       

    8. **Fluids:**  
       - Fluid statics: pressure, density, and buoyant force.  
       - Fluid dynamics: continuity equation and Bernoulli’s principle.  
      

    Type `!physformulas ` to see important formulas!
    Type `!physunit1` to study unit 1!
    Type `!physunit2` to study unit 2!
    Type `!physunit3` to study unit 3!
    Type `!physunit4` to study unit 4!
    Type `!physunit5` to study unit 5!
    Type `!physunit6` to study unit 6!
    Type `!physunit7` to study unit 7!
    Type `!physunit8` to study unit 8!
    Type `!physpractice` to get access to practice problems!  
    Type `!physstudyguide` to get access to an exclusive study guide!  
    """)
    await asyncio.sleep(1)

@bot.command()
async def physformulas(ctx):
    await ctx.send("""**AP Physics Formulas**
    1. **Kinematics:**
       - `v = u + at`
       - `s = ut + 0.5at²`
       - `v² = u² + 2as`
       2. **Force and Translational Dynamics:**
       - `F = ma`
       3. **Work, Energy, and Power:**
       - `W = Fd`
       - `KE = 0.5mv²`
       - `PE = mgh`
       4. **Linear Momentum:**
       - `p = mv`
       5. **Torque and Rotational Dynamics:**
       - `τ = r × F`
       6. **Energy and Momentum of Rotating Systems:**
       - `KE_rot = 0.5Iω²`
       7. **Oscillations:**
       - `T = 2π√(m/k)`
       8. **Fluids:**
       - `P = ρgh`
       - `Fb = ρVg`
       """)
    await asyncio.sleep(1)

    
@bot.command()
async def physunit1(ctx):
    await ctx.send("""**AP Physics Unit 1: Kinematics**
    1. **Motion in One Dimension:**
       - Displacement, velocity, and acceleration.
       - Equations of motion: `v = u + at`, `s = ut + 0.5at²`, `v² = u² + 2as`.
       - Graphical analysis: position-time and velocity-time graphs.
       2. **Projectile Motion:**
       - Horizontal and vertical components of motion.
       - Range and maximum height of projectiles.
       - Trajectories and angles of launch. 
           """)
    await asyncio.sleep(1)

@bot.command()
async def physunit2(ctx):
    await ctx.send("""**AP Physics Unit 2: Force and Translational Dynamics**
    1. **Newton’s Laws of Motion**
       - First law: Inertia and the concept of mass.
       - Second law: Force and acceleration (`F = ma`).
       - Third law: Action and reaction forces.
    2. **Free-Body Diagrams:**
       - Drawing and analyzing free-body diagrams.
       - Identifying forces acting on an object.
    3. **Friction:**
       - Static and kinetic friction.
       - Coefficient of friction and normal force.
    4. **Tension and Applied Forces:**
       - Tension in strings and ropes.
       - Applied forces and their effects on objects.
    """)
    await asyncio.sleep(1)

@bot.command()
async def physunit3(ctx):
    await ctx.send("""**AP Physics Unit 3: Work, Energy, and Power**
    1. **Work-Energy Theorem:**
       - Work done by a constant force.
       - Kinetic energy and potential energy.
    2. **Conservation of Energy:**
       - Energy conservation in various systems.
       - Energy transformations.
    3. **Power:**
       - Definition and calculation of power.
       - Mechanical advantage and efficiency.
    """)
    await asyncio.sleep(1)

@bot.command()
async def physunit4(ctx):
    await ctx.send("""**AP Physics Unit 4: Linear Momentum**
    1. **Impulse-Momentum Theorem:**
       - Impulse and change in momentum.
       - Conservation of momentum.
    2. **Collisions:**
       - Elastic and inelastic collisions.
       - Coefficient of restitution.
    3. **Center of Mass:**
       - Motion of a system of particles.
       - Center of mass and its properties.
    """)
    await asyncio.sleep(1)

@bot.command()
async def physunit5(ctx):
    await ctx.send("""**AP Physics Unit 5: Torque and Rotational Dynamics**
    1. **Rotational Motion:**
       - Angular velocity, angular acceleration, and moment of inertia.
       - Rotational kinetic energy.
    2. **Torque:**
       - Definition and calculation of torque.
       - Newton’s second law for rotation (`τ = Iα`).
    3. **Conservation of Angular Momentum:**
       - Angular momentum and its conservation.
       - Relationship between torque and angular acceleration.
    """)
    await asyncio.sleep(1)

@bot.command()
async def physunit6(ctx):
    await ctx.send("""**AP Physics Unit 6: Energy and Momentum of Rotating Systems**
    1. **Rotational Kinetic Energy:**
       - Comparison between rotational and linear kinetic energy.
       - Moment of inertia and rotational kinetic energy.
    2. **Angular Momentum:**
       - Definition and conservation of angular momentum.
       - Relationship between torque and angular momentum.
    3. **Rotational Dynamics:**
       - Torque and angular acceleration.
       - Work done by a torque.
    """)
    await asyncio.sleep(1)

@bot.command()
async def physunit7(ctx):
    await ctx.send("""**AP Physics Unit 7: Oscillations**
    1. **Simple Harmonic Motion (SHM):**
       - Springs and pendulums as examples of SHM.
       - Period and frequency of oscillations.
    2. **Energy in Oscillating Systems:**
       - Kinetic and potential energy in SHM.
       - Damping and energy loss.
    3. **Forced Oscillations:**
       - Driven and damped oscillations.
       - Resonance and amplitude.
    """)
    await asyncio.sleep(1)

@bot.command()
async def physunit8(ctx):
    await ctx.send("""**AP Physics Unit 8: Fluids**
    1. **Fluid Statics:**
       - Pressure, density, and buoyant force.
       - Pascal’s principle and applications.
    2. **Fluid Dynamics:**
       - Continuity equation and Bernoulli’s principle.
       - Applications of fluid dynamics.
    3. **Viscosity and Flow:**
       - Viscosity and its effects on fluid flow.
       - Laminar and turbulent flow.
    """)
    await asyncio.sleep(1)

@bot.command()
async def physpractice(ctx):
    await ctx.send("""**AP Physics Practice Questions**
    1. **Kinematics:**
       - A car travels 100 meters in 5 seconds. What is its average velocity?
       - A ball is thrown vertically upward with an initial velocity of 20 m/s. What is its maximum height?
       2. **Force and Translational Dynamics:**
       - A 5 kg object is accelerated at 2 m/s². What force is acting on it?
       - A 10 kg box is pushed across a floor with a force of 20 N. What is its acceleration?
       3. **Work, Energy, and Power:**
       - A 2 kg object is lifted 5 meters. What work is done?
       - A 100 W lightbulb is on for 1 hour. How much energy does it consume?
       4. **Linear Momentum:**
       - A 5 kg ball is moving at 10 m/s. What is its momentum?
       - Two objects collide elastically. What is the final velocity of each object?
       5. **Torque and Rotational Dynamics:**
       - A 2 kg object is rotating with an angular velocity of 5 rad/s. What is its moment of inertia?
       - A 10 N·m torque is applied to a 5 kg object. What is its angular acceleration?
       6. **Energy and Momentum of Rotating Systems:**
       - A 5 kg object is rotating with an angular velocity of 5 rad/s. What is its rotational kinetic energy?
       - A 10 N·m torque is applied to a 5 kg object. What is its angular momentum?
       7. **Oscillations:**
       - A spring has a natural frequency of 5 Hz. What is its period?
       - A pendulum has a period of 2 seconds. What is its length?
       8. **Fluids:**
       - A 10 kg object is submerged in water. What is its buoyant force?
       - A 5 m³ tank of water is filled to the brim. What is its pressure at the bottom?
    """)
    await asyncio.sleep(1)

@bot.command()
async def physstudyguide(ctx):
    await ctx.send("""**AP Physics Study Guide**
    https://uploads-ssl.webflow.com/605fe570e5454a357d1e1811/60a02f53cf4e686266e82f10_SS-AP-Physics-1.pdf
    """)
    await asyncio.sleep(1)

@bot.command()
async def APES(ctx):
    await ctx.send("""**AP Environmental Science Topics to Study**
    **Unit 1: The Living World: Ecosystems**
    - Ecosystem Structure: Biotic and abiotic components
    - Energy Flow: Food chains, food webs, and trophic levels
    - Nutrient Cycles: Carbon, nitrogen, phosphorus, and water cycles
    - Ecosystem Productivity: Primary and net productivity

    **Unit 2: The Living World: Biodiversity**
    - Genetic, Species, and Ecosystem Diversity
    - Natural Selection and Evolution
    - Island Biogeography and Habitat Fragmentation
    - Conservation Efforts and Endangered Species

    **Unit 3: Populations**
    - Population Dynamics: Growth rates, carrying capacity
    - Age Structure Diagrams and Population Pyramids
    - Reproductive Strategies (r-selected vs. K-selected species)
    - Human Population Impacts: Demographic transition

    **Unit 4: Earth Systems and Resources**
    - Soil Composition and Formation
    - Watersheds and Water Cycle
    - Geological Processes: Plate tectonics, earthquakes, volcanoes
    - Atmospheric Layers and Climate Patterns

    **Unit 5: Land and Water Use**
    - Agriculture and Food Production: Sustainable practices
    - Forestry and Logging: Clear-cutting vs. selective logging
    - Urban Development and Land Conservation
    - Mining and Resource Extraction

    **Unit 6: Energy Resources and Consumption**
    - Renewable vs. Nonrenewable Energy Sources
    - Energy Efficiency and Consumption Trends
    - Environmental Consequences of Energy Use
    - Alternative Energy Technologies (solar, wind, nuclear)

    **Unit 7: Atmospheric Pollution**
    - Primary and Secondary Pollutants
    - Acid Rain and its Effects
    - Photochemical Smog and Urban Air Quality
    - Regulatory Policies: Clean Air Act

    **Unit 8: Aquatic and Terrestrial Pollution**
    - Water Pollution Sources: Point vs. nonpoint
    - Waste Management: Landfills, composting, recycling
    - Eutrophication and Dead Zones
    - Soil Degradation and Desertification

    **Unit 9: Global Change**
    - Climate Change: Causes, evidence, and impacts
    - Greenhouse Gases and Global Warming
    - Ozone Depletion and Mitigation Efforts
    - Environmental Policies: Paris Agreement, Kyoto Protocol

    Type `!apesvocab` to see important terms!
    Type `apesunit1` to study unit 1!
    Type `apesunit2` to study unit 2!
    Type `apesunit3` to study unit 3!
    Type `apesunit4` to study unit 4!
    Type `apesunit5` to study unit 5!
    Type `apesunit6` to study unit 6!
    Type `apesunit7` to study unit 7!
    Type `apesunit8` to study unit 8!
    Type `apesunit9` to study unit 9!
    Type `!apesstudyguide` to get access to an exclusive study guide!
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesvocab(ctx):
    await ctx.send("""**AP Environmental Science Vocabulary**
    1. **Biodiversity:** The variety of life in the world or a particular ecosystem.
    2. **Carrying Capacity:** The maximum population size that an environment can sustain.
    3. **Ecosystem Services:** Benefits provided by ecosystems to humans, such as clean water and pollination.
    4. **Trophic Levels:** The levels in a food chain through which energy flows.
    5. **Biomagnification:** Increase in concentration of pollutants in organisms higher up the food chain.
    6. **Greenhouse Effect:** Trapping of heat in the Earth's atmosphere by greenhouse gases.
    7. **Ecological Footprint:** A measure of human demand on Earth's ecosystems.
    8. **Sustainability:** Meeting the needs of the present without compromising future generations.
    9. **Keystone Species:** A species on which other species in an ecosystem largely depend.
    10. **Tragedy of the Commons:** Overexploitation of a shared resource.
    11. **NIMBY (Not In My Backyard):** Opposition by residents to a proposal for a new development because it is close to them.
    12. **Biogeochemical Cycles:** Pathways by which chemical elements move through both biotic and abiotic components.
    13. **Photochemical Smog:** Air pollution that forms from the interaction between chemicals in the air and sunlight.
    14. **Nonrenewable Resource:** A natural resource that cannot be readily replaced.
    15. **Renewable Resource:** A resource that can be replenished naturally over time.
    16. **Point Source Pollution:** Pollution that comes from a single, identifiable source.
    17. **Nonpoint Source Pollution:** Pollution that comes from many diffuse sources.
    18. **Eutrophication:** Excessive nutrients in a body of water causing dense plant growth and death of animal life.
    19. **Mitigation:** Strategies to reduce the severity of climate change.
    20. **Restoration Ecology:** The practice of renewing and restoring degraded ecosystems.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesunit1(ctx):
    await ctx.send("""**AP Environmental Science Unit 1: The Living World: Ecosystems**
    1. **Ecosystem Structure:**
       - Biotic components: Plants, animals, and microorganisms.
       - Abiotic components: Soil, water, air, and climate.
    2. **Energy Flow:**
       - Food chains and food webs.
       - Trophic levels and energy transfer.
    3. **Nutrient Cycles:**
       - Carbon cycle: Photosynthesis, respiration, and decomposition.
       - Nitrogen cycle: Fixation, nitrification, and denitrification.
       - Phosphorus cycle: Weathering, erosion, and deposition.
       - Water cycle: Evaporation, condensation, and precipitation.
    4. **Ecosystem Productivity:**
       - Primary productivity: Photosynthesis.
       - Net productivity: Gross primary productivity minus respiration.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesunit2(ctx):
    await ctx.send("""**AP Environmental Science Unit 2: The Living World: Biodiversity**
    1. **Genetic, Species, and Ecosystem Diversity:**
       - Genetic diversity: Variation in genes within a population.
       - Species diversity: Number of species in an ecosystem.
       - Ecosystem diversity: Variety of habitats and niches.
    2. **Natural Selection and Evolution:**
       - Charles Darwin and the theory of evolution.
       - Mechanisms of evolution: Mutation, genetic drift, and gene flow.
    3. **Island Biogeography and Habitat Fragmentation:**
       - Island biogeography: Species richness and endemism.
       - Habitat fragmentation: Effects on biodiversity and ecosystem services.
    4. **Conservation Efforts and Endangered Species:**
       - IUCN Red List and conservation status.
       - Habitat protection and restoration.
       - Captive breeding and reintroduction programs.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesunit3(ctx):
    await ctx.send("""**AP Environmental Science Unit 3: Populations**
    1. **Population Dynamics:**
       - Growth rates: Exponential, logistic, and zero growth.
       - Carrying capacity: Maximum population size an environment can sustain.
    2. **Age Structure Diagrams and Population Pyramids:**
       - Age structure diagrams: Distribution of individuals by age.
       - Population pyramids: Age and sex distribution of a population.
    3. **Reproductive Strategies:**
       - r-selected species: High reproductive rate, short lifespan.
       - K-selected species: Low reproductive rate, long lifespan.
    4. **Human Population Impacts:**
       - Demographic transition: Shift from high birth and death rates to low birth and death rates.
       - Overpopulation and resource depletion.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesunit4(ctx):
    await ctx.send("""**AP Environmental Science Unit 4: Earth Systems and Resources**
    1. **Soil Composition and Formation:**
       - Soil horizons: O, A, B, C, and R horizons.
       - Soil formation factors: Climate, organisms, topography, parent material, and time.
    2. **Watersheds and Water Cycle:**
       - Watersheds: Areas drained by a river system.
       - Water cycle: Evaporation, condensation, precipitation, and runoff.
    3. **Geological Processes:**
       - Plate tectonics: Plate boundaries and plate movements.
       - Earthquakes: Causes, types, and effects.
       - Volcanoes: Types, eruptions, and hazards.
    4. **Atmospheric Layers and Climate Patterns:**
       - Atmospheric layers: Troposphere, stratosphere, mesosphere, thermosphere, and exosphere.
       - Climate patterns: El Niño-Southern Oscillation, monsoons, and hurricanes.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesunit5(ctx):
    await ctx.send("""**AP Environmental Science Unit 5: Land and Water Use**
    1. **Agriculture and Food Production:**
       - Sustainable practices: Crop rotation, conservation tillage, and integrated pest management.
       - Food security and hunger.
    2. **Forestry and Logging:**
       - Clear-cutting vs. selective logging.
       - Forest management and conservation.
    3. **Urban Development and Land Conservation:**
       - Urban sprawl and land use changes.
       - Conservation efforts: National parks, wildlife refuges, and protected areas.
    4. **Mining and Resource Extraction:**
       - Surface and underground mining.
       - Environmental impacts: Soil erosion, water pollution, and habitat destruction.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesunit6(ctx):
    await ctx.send("""**AP Environmental Science Unit 6: Energy Resources and Consumption**
    1. **Renewable vs. Nonrenewable Energy Sources:**
       - Renewable: Solar, wind, hydro, geothermal, and biomass.
       - Nonrenewable: Fossil fuels (coal, oil, natural gas) and nuclear.
    2. **Energy Efficiency and Consumption Trends:**
       - Energy conservation: Insulation, efficient appliances, and renewable energy.
       - Energy consumption trends: Global energy demand and supply.
    3. **Environmental Consequences of Energy Use:**
       - Air and water pollution.
       - Climate change and greenhouse gas emissions.
       - Resource depletion and land use changes.
    4. **Alternative Energy Technologies:**
       - Solar energy: Photovoltaic and concentrated solar power.
       - Wind energy: Wind turbines and offshore wind farms.
       - Nuclear energy: Fission and fusion.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesunit7(ctx):
    await ctx.send("""**AP Environmental Science Unit 7: Atmospheric Pollution**
    1. **Primary and Secondary Pollutants:**
       - Primary pollutants: SO₂, NOₓ, CO, and particulate matter.
       - Secondary pollutants: O₃, PM₂.₅, and NO₂.
    2. **Acid Rain and its Effects:**
       - Causes: SO₂ and NOₓ emissions.
       - Effects: Acidification of soil and water, damage to ecosystems, and health impacts.
    3. **Photochemical Smog and Urban Air Quality:**
       - Causes: Volatile organic compounds (VOCs) and NOₓ.
       - Effects: Respiratory and cardiovascular diseases, visibility reduction, and crop damage.
    4. **Regulatory Policies:**
       - Clean Air Act: Emission standards, monitoring, and enforcement.
       - Air quality indices (AQI) and health guidelines.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesunit8(ctx):
    await ctx.send("""**AP Environmental Science Unit 8: Aquatic and Terrestrial Pollution**
    1. **Water Pollution Sources:**
       - Point sources: Pipes, factories, and sewage treatment plants.
       - Nonpoint sources: Agriculture, urban runoff, and atmospheric deposition.
    2. **Waste Management:**
       - Landfills: Composition, leachate, and methane emissions.
       - Composting and recycling: Benefits and challenges.
    3. **Eutrophication and Dead Zones:**
       - Causes: Nutrient runoff and wastewater discharge.
       - Effects: Algal blooms, hypoxia, and fish kills.
    4. **Soil Degradation and Desertification:**
       - Causes: Deforestation, overgrazing, and climate change.
       - Effects: Soil erosion, loss of biodiversity, and reduced agricultural productivity.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesunit9(ctx):
    await ctx.send("""**AP Environmental Science Unit 9: Global Change**
    1. **Climate Change:**
       - Causes: Greenhouse gas emissions, deforestation, and land use changes.
       - Evidence: Global temperature rise, sea level rise, and extreme weather events.
       - Impacts: Ecosystem shifts, human health, and economic losses.
    2. **Greenhouse Gases and Global Warming:**
       - Major greenhouse gases: CO₂, CH₄, N₂O, and H₂O vapor.
       - Global warming potential (GWP) and atmospheric lifetime.
    3. **Ozone Depletion and Mitigation Efforts:**
       - Causes: Chlorofluorocarbons (CFCs) and halons.
       - Effects: Increased UV radiation, skin cancer, and immune system suppression.
       - Mitigation efforts: Montreal Protocol and ozone-friendly alternatives.
    4. **Environmental Policies:**
       - Paris Agreement: Nationally determined contributions (NDCs) and global goals.
       - Kyoto Protocol: Emission reduction targets and international cooperation.
    """)
    await asyncio.sleep(1)

@bot.command()
async def apesstudyguide(ctx):
    await ctx.send("""**AP Environmental Science Study Guide**
   https://uploads-ssl.webflow.com/605fe570e5454a357d1e1811/60a02be2f3b25f044ccddca1_SS-AP-Env-Sci.pdf
    """)
    await asyncio.sleep(1)

@bot.command()
async def APCSA(ctx):
    part_1 = ("""**AP Computer Science A Topics to Study**
    1. **Primitive Types:**  
       - Variables, data types (int, double, boolean), expressions, and casting.  

    2. **Using Objects:**  
       - Creating and using objects, calling methods, and understanding method signatures.  
       - String methods, the Math class, and object references.  

    3. **Boolean Expressions and if Statements:**  
       - Relational operators, boolean expressions, and conditional statements (if, else if, else).  

    4. **Iteration:**  
       - Loops (for, while, do-while) and nested loops.  
       - Traversing arrays and ArrayLists using loops.  

    5. **Writing Classes:**  
       - Defining classes, constructors, and methods.  
       - Instance variables, encapsulation, and accessors/mutators.  
       - Overloading methods and constructors.  

    6. **Array:**  
       - Declaring, initializing, and accessing elements in arrays.  
       - Iterating through arrays and performing basic operations.  
       - Searching and sorting algorithms.  
       """)
    await ctx.send(part_1)
    await asyncio.sleep(1)  # Pause before sending the next part

    part_2 = ("""7. **ArrayList:**  
       - Using ArrayLists to store, add, remove, and manipulate elements.  

    8. **2D Array:**  
       - Creating, initializing, and accessing elements in two-dimensional arrays.  
       - Iterating through rows and columns using nested loops.  

    9. **Inheritance:**  
       - Creating subclasses, using super() and overriding methods.  
       - The "is-a" relationship, polymorphism, and dynamic method binding.  
       - Abstract classes and interfaces.  

    10. **Recursion:**  
        - Writing and tracing recursive methods.  
        - Understanding base cases, recursive calls, and recursion depth.  
        - Common recursive algorithms (factorial, Fibonacci, binary search).  
   
Type `!csavocab` to see important terms!
 Type `!csaunit1` to study unit 1!
    Type `!csaunit2` to study unit 2!
    Type `!csaunit3` to study unit 3!
    Type `!csaunit4` to study unit 4!
    Type `!csaunit5` to study unit 5!
    Type `!csaunit 6` to study unit 6!
    Type `!csaunit7` to study unit 7!
    Type `!csaunit8` to study unit 8!
    Type `!csaunit9` to study unit 9!
    Type `!csaunit10` to study unit 10!
    Type `!csastudyguide` to get access to an exclusive study guide!
    
        """)
    await ctx.send(part_2)

@bot.command()
async def csavocab(ctx):
    await ctx.send("""**AP Computer Science A Vocabulary**
    **Class**: A blueprint for creating objects, providing initial values for fields and methods.  
    **Object**: An instance of a class that holds data and methods.  
    **Method**: A function defined inside a class that defines behavior.  
    **Constructor**: A special method used to initialize new objects.  
    **Inheritance**: Mechanism where one class acquires the properties of another.  
    **Encapsulation**: Bundling data and methods within a class, restricting direct access.  
    **Polymorphism**: Concept where objects can take many forms through inheritance.  
    **Abstraction**: Hiding internal details and showing only essential features.  
    **Interface**: A contract for classes to implement specific methods.  
    **Array**: A container that holds a fixed number of values of a single type.  
    **ArrayList**: A resizable array from the Java Collections Framework.  
    **Loop**: Repeats a block of code while a condition is true (`for`, `while`).  
    **Conditional**: Executes code based on Boolean expressions (`if`, `else`).  
    **Recursion**: A method that calls itself to solve a problem.  
    **Static**: Belongs to the class rather than any object instance.  
    **Public**: Access modifier that allows visibility everywhere.  
    **Private**: Access modifier that restricts visibility to the class only.  
    **Null**: A value that indicates no object is referenced.  
    **Compile-time error**: Detected by the compiler, such as syntax issues.  
    **Runtime error**: Occurs while the program is running, like division by zero.
    """)
    await asyncio.sleep(1)

@bot.command()
async def csaunit1(ctx):
   await ctx.send("""**APCSA Unit 1: Primitive Types**

**Primitive Type**: A basic data type not created from a class (e.g., `int`, `double`, `boolean`, `char`).  
**int**: Integer type; whole numbers (e.g., 5, -3, 0).  
**double**: Decimal number type; floating-point numbers (e.g., 3.14, -0.001).  
**boolean**: Holds one of two values: `true` or `false`.  
**char**: A single 16-bit Unicode character (e.g., `'a'`, `'Z'`).  
**String**: A sequence of characters (not primitive, but commonly used).  
**Declaration**: Creating a variable (e.g., `int x;`).  
**Initialization**: Giving a variable its first value (e.g., `x = 5;`).  
**Assignment**: Giving a variable a value or updating it (e.g., `x = 10;`).  
**Expression**: A combination of variables, operators, and values that produces a result.  
**Operator**: Symbol that performs an operation (e.g., `+`, `-`, `*`, `/`, `%`).  
**Casting**: Manually converting one data type to another (e.g., `(int) 3.14`).  
**Overflow**: When a value exceeds the storage capacity of its type.  
**Literal**: A fixed value written directly into the code (e.g., `42`, `true`, `'c'`).  
**Concatenation**: Joining strings using the `+` operator.""")
   await asyncio.sleep(1)

@bot.command()
async def csaunit2(ctx):
    await ctx.send ("""**APCSA Unit 2: Using Objects**

**Object**: An instance of a class; contains data (fields) and behavior (methods).  
**Class**: A blueprint for creating objects.  
**Constructor**: A special method used to initialize new objects (e.g., `new Scanner(System.in);`).  
**Method Call**: Invoking a method using dot notation (e.g., `str.length()`).  
**Return Type**: The type of value a method gives back (e.g., `int`, `String`).  
**Void**: A return type indicating the method does not return a value.  
**Parameters**: Inputs specified in a method’s definition.  
**Arguments**: Values passed into a method when it is called.  
**String Methods**:  
- `length()` – returns number of characters  
- `substring(a, b)` – returns substring from index `a` to `b - 1`  
- `indexOf(str)` – returns the index of the first occurrence of `str`  
**Math Methods** (from `Math` class):  
- `Math.abs(x)` – absolute value  
- `Math.pow(x, y)` – x raised to power y  
- `Math.sqrt(x)` – square root  
- `Math.random()` – returns a double from 0.0 to just under 1.0  
**Import Statement**: Used to bring in predefined classes (e.g., `import java.util.Scanner;`).  
**Scanner Class**: Allows for user input (e.g., `Scanner input = new Scanner(System.in);`).
""")
    await asyncio.sleep(1)

@bot.command()
async def csaunit3(ctx):
   await ctx.send ("""**APCSA Unit 3: Boolean Expressions and If Statements**

**boolean**: A true or false value.  
**==**: Equal to  
**!=**: Not equal to  
**<, >, <=, >=**: Comparison operators  
**&&**: AND  
**||**: OR  
**!**: NOT (opposite)  
**if**: Runs code only if a condition is true  
**if-else**: Runs one block if true, another if false  
**else-if**: Checks multiple conditions in order  
**Short-circuiting**: Java stops checking once the answer is known  
**De Morgan’s Laws**: Rules to simplify NOT statements:  
- `!(A && B)` → `!A || !B`  
- `!(A || B)` → `!A && !B`
""")
   await asyncio.sleep(1)

@bot.command
async def csaunit4(ctx):
   await ctx.sendf (""" **APCSA Unit 4: Iteration**

**Iteration**: Repeating a block of code multiple times (looping).  
**for loop**: Loops a known number of times.  
```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}""")
   await asyncio.sleep(1)

@bot.command
async def csaunit5(ctx):
   await ctx.send ("""**APCSA Unit 5: Writing Classes**

**Class**: A blueprint for creating objects with fields and methods.  
**Instance Variable (Field)**: Variables that belong to each object.  
**Constructor**: Special method to initialize new objects.  
**this**: Keyword that refers to the current object.  
**Accessor Method (Getter)**: Returns the value of an instance variable.  
**Mutator Method (Setter)**: Sets or updates the value of an instance variable.  
**Method Overloading**: Defining multiple methods with the same name but different parameters.  
**Encapsulation**: Keeping instance variables private and controlling access via methods.  
**Private**: Access modifier restricting visibility to within the class.  
**Public**: Access modifier allowing visibility everywhere.  
**Return Statement**: Ends a method and optionally sends back a value.  
**Void Method**: A method that does not return a value.

Example constructor:  
```java
public class Car {
    private String model;

    public Car(String model) {
        this.model = model;
    }
}""")
   await asyncio.sleep(1)

@bot.command()
async def csaunit6(ctx):
   await ctx.send ("""**APCSA Unit 6: Arrays**

**Array**: A container that holds a fixed number of values of the same type.  
**Index**: The position of an element in an array (starts at 0).  
**Length**: The size of the array (`array.length`).  
**Declaration**: Creating an array variable (e.g., `int[] nums;`).  
**Initialization**: Allocating memory for the array (e.g., `nums = new int[5];`).  
**Access**: Getting or setting an element using its index (e.g., `nums[0] = 10;`).  
**Traversal**: Looping through all elements in an array.  
**Off-by-one error**: Accessing an index outside the valid range (`0` to `length - 1`).  
**Enhanced for loop** (for-each loop): Simplifies traversal of arrays.  
```java
for (int num : nums) {
    System.out.println(num);
}""")
   await asyncio.sleep(1)

@bot.command()
async def csaunti7(ctx):
   await ctx.send ("""**APCSA Unit 7: ArrayLists**

**ArrayList**: A resizable array (from `java.util.ArrayList`) that can grow or shrink dynamically.  
**Import Statement**: `import java.util.ArrayList;` needed to use ArrayLists.  
**Generic Type**: Specifies the type of elements in the ArrayList (e.g., `ArrayList<String>`).  
**Add**: Adds an element to the end (`add(element)`).  
**Add at Index**: Inserts an element at a specific index (`add(index, element)`).  
**Remove**: Removes an element by index or object (`remove(index)` or `remove(object)`).  
**Get**: Returns the element at a given index (`get(index)`).  
**Set**: Replaces the element at a specific index (`set(index, element)`).  
**Size**: Returns the number of elements in the list (`size()`).  
**IndexOutOfBoundsException**: Runtime error when accessing invalid indices.  
**Traversal**: Looping through the ArrayList, typically with a `for` loop or enhanced for loop.  
**Dynamic resizing**: Unlike arrays, ArrayLists automatically resize when elements are added or removed.

Example:  
```java
ArrayList<String> list = new ArrayList<>();
list.add("apple");
String fruit = list.get(0);""")
   await asyncio.sleep(1)

@bot.command()
async def csaunit8(ctx):
   await ctx.send ("""
   **APCSA Unit 8: 2D Arrays**

   **2D Array**: An array of arrays, like a grid or table (rows and columns).  
   **Declaration**: `int[][] matrix;`  
   **Initialization**: `matrix = new int[3][4];` creates 3 rows and 4 columns.  
   **Access**: Use two indices: `matrix[row][column]`  
   **Traversal**: Nested loops to go through rows and columns.  
   ```java
   for (int i = 0; i < matrix.length; i++) {
       for (int j = 0; j < matrix[i].length; j++) {
           System.out.print(matrix[i][j] + " ");
       }
       System.out.println();
   }
   """)
   await asyncio.sleep(1)

@bot.command
async def csaunit9(ctx):
   await ctx.send("""
   **APCSA Unit 9: Inheritance and Polymorphism**

   **Inheritance**: A mechanism where one class (subclass) acquires properties and methods from another class (superclass).  
   **Subclass**: The class that inherits from another class.  
   **Superclass**: The class being inherited from.  
   **extends**: Keyword used to declare inheritance.  
   ```java
   public class Dog extends Animal {
       // Dog inherits from Animal
   }
   """)
   await asyncio.sleep(1)

@bot.command()
async def csaunit10(ctx):
    await ctx.send("""
   **APCSA Unit 10: Recursion**

   **Recursion**: When a method calls itself to solve a problem by breaking it into smaller subproblems.  
   **Base Case**: The condition where the recursion stops.  
   **Recursive Case**: The part of the method where it calls itself with modified parameters.  
   **Stack Overflow**: An error caused by too many recursive calls without reaching the base case.  
   **Trace**: The sequence of method calls during recursion.  
   **Divide and Conquer**: Breaking a problem into smaller pieces, solving each recursively, and combining results.

   Example (Factorial):
   ```java
   public int factorial(int n) {
       if (n == 0) return 1;      // Base case
       else return n * factorial(n - 1);  // Recursive case
   }
   """)
    await asyncio.sleep(1)

@bot.command()
async def csastudyguide(ctx):
    await ctx.send("""**AP Computer Science A Study Guide**
   https://www.simplestudies.org/groups/ap-computer-science-a
    """)
    await asyncio.sleep(1)             

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    # Set bot's status to display the !studyhelp command
    await bot.change_presence(activity=discord.Game(name="!aphelp"))

bot.run(token)
