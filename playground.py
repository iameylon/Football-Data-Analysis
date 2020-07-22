# מה הסיכוי של קבוצה לנצח אם היא הובילה בx שערים במחצית?
# למשל בשער אחד 70% לנצח, 2 ב80% וכן הלאה. הפרש שערים במחצית על סיכוי הקבוצה לנצח. גרף עמודות. ואם היא בבית לעומת חוץ?

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.figure import Figure
from scipy import stats
from scipy.stats import ttest_1samp
from Leagues_Data_and_Adaptations import laLiga0919Filtered2
from English_Premier_League_Data_and_Adaptations import premierLeague9518Filtered2


# Bar graph of Half-Time-leader's status at Final Time result
def HT_leader_status_at_FT_bar_plot_comparison(league_df_1):
    plt.close()
    num_of_games_that_have_lead_at_HT = len(league_df_1)
    num_of_games_that_leader_wins_at_FT = len(league_df_1[league_df_1.FTR == league_df_1.HTR])
    num_of_games_that_draw_at_FT = len(league_df_1[league_df_1.FTR == 'D'])
    num_of_games_that_leader_loses_at_FT = num_of_games_that_have_lead_at_HT - num_of_games_that_leader_wins_at_FT - num_of_games_that_draw_at_FT

    colors = ["g", "c", "r"]
    leaderStatus = ["Leader Won", "Leader Drew", "Leader Lost"]
    percentages = [(num_of_games_that_leader_wins_at_FT / num_of_games_that_have_lead_at_HT) * 100,
                   (num_of_games_that_draw_at_FT / num_of_games_that_have_lead_at_HT) * 100,
                   (num_of_games_that_leader_loses_at_FT / num_of_games_that_have_lead_at_HT) * 100]
    fig, ax = plt.subplots()
    ax.bar(leaderStatus, percentages, color=colors[:len(percentages)])
    for index, value in enumerate(percentages):
        ax.text(x=index - 0.37, y=value + .25, s=str(value), color='black', fontweight='bold', size=8)

    plt.title("Half-Time-Leader' result at Final-Time")
    plt.ylabel("Percents")
    plt.xlabel("Leader's Status")
    plt.margins(y=0.1)
    plt.tight_layout()
    plt.show()


HT_leader_status_at_FT_bar_plot_comparison(laLiga0919Filtered2)
HT_leader_status_at_FT_bar_plot_comparison(premierLeague9518Filtered2)
