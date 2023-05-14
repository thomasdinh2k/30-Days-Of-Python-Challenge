Valorant_agents = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 'Jett', 'Kay/O', 'Killjoy', 'Neon',
                   'Omen', 'Phoenix',
                   'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']
Lol_champions = (
    "Annie",
    "Ahri",
    "Akali",
    "Alistar",
    "Amumu",
    "Anivia",
    "Ashe",
    "Aurelion Sol",
    "Azir",
    "Bard",
    "Blitzcrank",
    "Brand",
    "Braum",
    "Caitlyn",
    "Camille",
    "Cho'Gath",
    "Corki",
    "Darius",
    "Diana",
    "Dr. Mundo",
)
test = False

if test is True:
    Valorant_agents = tuple((agent) for agent in Valorant_agents)

    print(type(Valorant_agents))
    print(f"There are {len(Valorant_agents)} Valorant Agents")

    Riot = Valorant_agents + Lol_champions
    print(Riot)
    print(type(Riot))
    print(' '.join([i for i in Riot]))  # Print tuple by using list comprehension

    Valorant_agents = list(Valorant_agents)
    Valorant_agents.append("Nekko")
    print("\n".join([champion for champion in Valorant_agents]))

    agent_1, agent_2, agent_3, *the_rest = Valorant_agents
    print(agent_1)
    print(the_rest)
else:
    print("Day 6 Completed")

