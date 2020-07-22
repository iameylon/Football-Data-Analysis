# מה הסיכוי של קבוצה לנצח אם היא הובילה בx שערים במחצית?
# למשל בשער אחד 70% לנצח, 2 ב80% וכן הלאה. הפרש שערים במחצית על סיכוי הקבוצה לנצח. גרף עמודות. ואם היא בבית לעומת חוץ?

# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms
# from scipy import stats
# from scipy.stats import ttest_1samp

from Leagues_Data_and_Adaptations import laLiga0919Filtered2
from Leagues_Data_and_Adaptations import premierLeague9518Filtered2

plt.style.use(['seaborn-white', 'bmh'])


#### Bar graph of Half-Time-leader's status at Final Time result
def HT_leader_status_at_FT_bar_plot_comparison(league_df_1, league_df_2):
    ind = np.arange(3)  # the x locations for the groups
    width = 0.27  # the width of the bars
    leaderStatus = np.array(["Leader Won", "Leader Drew", "Leader Lost"])

    ### parameters for 1st league:
    num_of_games_that_have_lead_at_HT_1 = len(league_df_1)
    num_of_games_that_leader_wins_at_FT_1 = len(league_df_1[league_df_1.FTR == league_df_1.HTR])
    num_of_games_that_draw_at_FT_1 = len(league_df_1[league_df_1.FTR == 'D'])
    num_of_games_that_leader_loses_at_FT_1 = num_of_games_that_have_lead_at_HT_1 - \
                                             num_of_games_that_leader_wins_at_FT_1 - \
                                             num_of_games_that_draw_at_FT_1
    percentages_for_1st = [(num_of_games_that_leader_wins_at_FT_1 / num_of_games_that_have_lead_at_HT_1) * 100,
                           (num_of_games_that_draw_at_FT_1 / num_of_games_that_have_lead_at_HT_1) * 100,
                           (num_of_games_that_leader_loses_at_FT_1 / num_of_games_that_have_lead_at_HT_1) * 100]

    ### parameters for 2nd league:
    num_of_games_that_have_lead_at_HT_2 = len(league_df_2)
    num_of_games_that_leader_wins_at_FT_2 = len(league_df_2[league_df_2.FTR == league_df_2.HTR])
    num_of_games_that_draw_at_FT_2 = len(league_df_2[league_df_2.FTR == 'D'])
    num_of_games_that_leader_loses_at_FT_2 = num_of_games_that_have_lead_at_HT_2 - \
                                             num_of_games_that_leader_wins_at_FT_2 - \
                                             num_of_games_that_draw_at_FT_2
    percentages_for_2nd = [(num_of_games_that_leader_wins_at_FT_2 / num_of_games_that_have_lead_at_HT_2) * 100,
                           (num_of_games_that_draw_at_FT_2 / num_of_games_that_have_lead_at_HT_2) * 100,
                           (num_of_games_that_leader_loses_at_FT_2 / num_of_games_that_have_lead_at_HT_2) * 100]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, percentages_for_1st, width, color='#07a64c')
    rects2 = ax.bar(ind + width * 1.1, percentages_for_2nd, width, color='#b7040e')

    ### Title, Labels, Legend
    ## Title
    plt.title("Half-Time-Leader's result at Final-Time")

    ## y label
    ax.set_ylabel("Percents")

    ## x label
    plt.xlabel("Leader's Status")
    ax.set_xticks(ind + width)
    ax.set_xticklabels(leaderStatus)

    plt.setp(ax.xaxis.get_majorticklabels())

    # Create offset transform by 5 points in x direction
    dx = -15 / 72.
    dy = 0 / 72.
    offset = matplotlib.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)

    # apply offset transform to all x ticklabels.
    for label in ax.xaxis.get_majorticklabels():
        label.set_transform(label.get_transform() + offset)
    ax.tick_params(axis='x', which='major', labelsize=8)
    ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=0)

    ## Legend
    ax.legend((rects1[0], rects2[0]), ("La Liga", "Premier League"))
    plt.margins(y=0.1)
    plt.tight_layout()

    ## bar labels
    def autolabel(rects):
        for rect in rects:
            rectHeight = rect.get_height()
            rectWidth = rect.get_width()
            ax.text(rect.get_x() + rectWidth / 2., 1.005 * rectHeight, '%g' % round(float(rectHeight), 2), ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    ## show
    plt.show()


HT_leader_status_at_FT_bar_plot_comparison(laLiga0919Filtered2, premierLeague9518Filtered2)
