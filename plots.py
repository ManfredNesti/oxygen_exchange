import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")
# plt.rcParams['text.usetex'] = True

def my_formatter(x, pos):
    if x == 0:
        return "0"
    else:
        return str(x)
    # if x.is_integer():
    #     return str(int(x))
    # else:
    #     return str(x)
formatter = FuncFormatter(my_formatter)

#########################################
# CBF 3
#########################################
mpl.rcParams.update({'font.size': 10})
CBF_at_rest = pd.read_csv('zygote/csv_files/normalized_velocity_profile_800_ms.csv')
CBF_covid = pd.read_csv('zygote/csv_files/normalized_velocity_profile_700_ms.csv')
CBF_stress = pd.read_csv('zygote/csv_files/normalized_velocity_profile_650_ms.csv')

plt.figure(figsize=(8,8), constrained_layout=False)
# plt.suptitle(title, fontsize=40, fontweight="bold")

# [5%, 44%, 70%]

# at rest [0.08, 0.352, 0.56]
ax1 = plt.subplot2grid(shape=(3,1), loc=(0,0))
ax1.plot(CBF_at_rest.t, CBF_at_rest.vel * 2, '-k', label='CBF')
ax1.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.08].t, CBF_at_rest[CBF_at_rest["t"] == 0.08].vel * 2, marker="o", edgecolors="black", color="blue", zorder=2) # t = 0.04 (5%)
ax1.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.352].t, CBF_at_rest[CBF_at_rest["t"] == 0.352].vel * 2, marker="o", edgecolors="black", color="red", zorder=2) # t = 0.04 (5%)
ax1.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.56].t, CBF_at_rest[CBF_at_rest["t"] == 0.56].vel * 2, marker="o", edgecolors="black", color="green", zorder=2) # t = 0.04 (5%)
# ax1.set_xlabel(r'Time [s]')
ax1.set_title(r'Patient at rest (HR: 75 bpm)')
ax1.set_xlim([0, 2.8]), ax1.set_ylim([-1, 2*2.12])
# ax1.xaxis.set_major_formatter(formatter)

# covid  [0.07, 0.308, 0.49]
ax2 = plt.subplot2grid(shape=(3,1), loc=(1,0), sharex=ax1)
ax2.plot(CBF_covid.t, CBF_covid.vel * 2, '-k', label='CBF')
ax2.scatter(CBF_covid[CBF_covid["t"] == 0.07].t, CBF_covid[CBF_covid["t"] == 0.07].vel * 2, marker="o", edgecolors="black", color="blue", zorder=2) # t = 0.04 (5%)
ax2.scatter(CBF_covid[CBF_covid["t"] == 0.308].t, CBF_covid[CBF_covid["t"] == 0.308].vel * 2, marker="o", edgecolors="black", color="red", zorder=2) # t = 0.04 (5%)
ax2.scatter(CBF_covid[CBF_covid["t"] == 0.49].t, CBF_covid[CBF_covid["t"] == 0.49].vel * 2, marker="o", edgecolors="black", color="green", zorder=2) # t = 0.04 (5%)
ax2.set_ylabel(r'$\Psi_{CBF}$ [cm$^3$ / s]')
ax2.set_xlim([0, 2.8]), ax2.set_ylim([-1, 2*2.12])
ax2.set_title(r'Patient affected by Sars-CoV-2 (HR: 85.7 bpm)')
# ax2.xaxis.set_major_formatter(formatter)

# stress [0.065, 0.286, 0.455]
ax3 = plt.subplot2grid(shape=(3,1), loc=(2,0), sharex=ax1)
ax3.plot(CBF_stress.t, CBF_stress.vel * 2, '-k', label='CBF')
ax3.scatter(CBF_stress[CBF_stress["t"] == 0.065].t, CBF_stress[CBF_stress["t"] == 0.065 ].vel * 2, marker="o", edgecolors="black", color="blue", zorder=2) # t = 0.04 (5%)
ax3.scatter(CBF_stress[CBF_stress["t"] == 0.286].t, CBF_stress[CBF_stress["t"] == 0.286].vel * 2, marker="o", edgecolors="black", color="red", zorder=2) # t = 0.04 (5%)
ax3.scatter(CBF_stress[CBF_stress["t"] == 0.455].t, CBF_stress[CBF_stress["t"] == 0.455].vel * 2, marker="o", edgecolors="black", color="green", zorder=2) # t = 0.04 (5%)
ax3.set_xlabel(r'Time [s]')# , ax3.set_ylabel(r'CBF [cm$^3$ / s]')
ax3.set_xlim([0, 2.8]), ax3.set_ylim([-1, 2*2.12])
ax3.set_title(r'Patient under physical activity (HR: 92.3 bpm)')
# ax3.xaxis.set_major_formatter(formatter)
plt.subplots_adjust(hspace=0.5)
plt.xticks(np.arange(0, 3.2, 0.4))
# for ax in [ax1, ax2]:
#     plt.setp(ax.get_xticklabels(), visible=False)
#     # The y-ticks will overlap with "hspace=0", so we'll hide the bottom tick
#     ax.set_yticks(ax.get_yticks()[1:])

# ax1.legend(), ax2.legend(), ax3.legend()

plt.savefig("Plots/CBF/CBF.pdf", transparent=True)

#########################################
# CBF 3 SLIDES
#########################################
mpl.rcParams.update({'font.size': 18})
CBF_at_rest = pd.read_csv('zygote/csv_files/normalized_velocity_profile_800_ms.csv')
CBF_covid = pd.read_csv('zygote/csv_files/normalized_velocity_profile_700_ms.csv')
CBF_stress = pd.read_csv('zygote/csv_files/normalized_velocity_profile_650_ms.csv')

plt.figure(figsize=(10,10), constrained_layout=False)
# plt.suptitle(title, fontsize=40, fontweight="bold")

# [5%, 44%, 70%]

# at rest [0.08, 0.352, 0.56]
ax1 = plt.subplot2grid(shape=(3,1), loc=(0,0))
ax1.plot(CBF_at_rest.t, CBF_at_rest.vel * 2, '-k', label='CBF')
ax1.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.08].t, CBF_at_rest[CBF_at_rest["t"] == 0.08].vel * 2, s=120, marker="o", edgecolors="black", color="blue", zorder=2) # t = 0.04 (5%)
ax1.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.352].t, CBF_at_rest[CBF_at_rest["t"] == 0.352].vel * 2, s=120,marker="o", edgecolors="black", color="red", zorder=2) # t = 0.04 (5%)
ax1.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.56].t, CBF_at_rest[CBF_at_rest["t"] == 0.56].vel * 2, s=120,marker="o", edgecolors="black", color="green", zorder=2) # t = 0.04 (5%)
# ax1.set_xlabel(r'Time [s]')
ax1.set_title(r'Patient at rest (HR: 75 bpm)')
ax1.set_xlim([0, 2.8]), ax1.set_ylim([-1, 2*2.14])
# ax1.xaxis.set_major_formatter(formatter)

# covid  [0.07, 0.308, 0.49]
ax2 = plt.subplot2grid(shape=(3,1), loc=(1,0), sharex=ax1)
ax2.plot(CBF_covid.t, CBF_covid.vel * 2, '-k', label='CBF')
ax2.scatter(CBF_covid[CBF_covid["t"] == 0.07].t, CBF_covid[CBF_covid["t"] == 0.07].vel * 2, s=120,marker="o", edgecolors="black", color="blue", zorder=2) # t = 0.04 (5%)
ax2.scatter(CBF_covid[CBF_covid["t"] == 0.308].t, CBF_covid[CBF_covid["t"] == 0.308].vel * 2, s=120,marker="o", edgecolors="black", color="red", zorder=2) # t = 0.04 (5%)
ax2.scatter(CBF_covid[CBF_covid["t"] == 0.49].t, CBF_covid[CBF_covid["t"] == 0.49].vel * 2, s=120,marker="o", edgecolors="black", color="green", zorder=2) # t = 0.04 (5%)
ax2.set_ylabel(r'$\Psi_{CBF}$ [cm$^3$ / s]')
ax2.set_xlim([0, 2.8]), ax2.set_ylim([-1, 2*2.14])
ax2.set_title(r'Patient affected by Sars-CoV-2 (HR: 85.7 bpm)')
# ax2.xaxis.set_major_formatter(formatter)

# stress [0.065, 0.286, 0.455]
ax3 = plt.subplot2grid(shape=(3,1), loc=(2,0), sharex=ax1)
ax3.plot(CBF_stress.t, CBF_stress.vel * 2, '-k', label='CBF')
ax3.scatter(CBF_stress[CBF_stress["t"] == 0.065].t, CBF_stress[CBF_stress["t"] == 0.065 ].vel * 2, s=120,marker="o", edgecolors="black", color="blue", zorder=2) # t = 0.04 (5%)
ax3.scatter(CBF_stress[CBF_stress["t"] == 0.286].t, CBF_stress[CBF_stress["t"] == 0.286].vel * 2, s=120,marker="o", edgecolors="black", color="red", zorder=2) # t = 0.04 (5%)
ax3.scatter(CBF_stress[CBF_stress["t"] == 0.455].t, CBF_stress[CBF_stress["t"] == 0.455].vel * 2, s=120,marker="o", edgecolors="black", color="green", zorder=2) # t = 0.04 (5%)
ax3.set_xlabel(r'Time [s]')# , ax3.set_ylabel(r'CBF [cm$^3$ / s]')
ax3.set_xlim([0, 2.8]), ax3.set_ylim([-1, 2*2.14])
ax3.set_title(r'Patient under physical activity (HR: 92.3 bpm)')
# ax3.xaxis.set_major_formatter(formatter)
plt.subplots_adjust(hspace=0.5)
plt.xticks(np.arange(0, 3.2, 0.4))
# for ax in [ax1, ax2]:
#     plt.setp(ax.get_xticklabels(), visible=False)
#     # The y-ticks will overlap with "hspace=0", so we'll hide the bottom tick
#     ax.set_yticks(ax.get_yticks()[1:])

# ax1.legend(), ax2.legend(), ax3.legend()

plt.savefig("Plots/CBF/CBF_slides.pdf", transparent=True)

#########################################
# CBF 1
#########################################
mpl.rcParams.update({'font.size': 12})
CBF_at_rest = pd.read_csv('zygote/csv_files/normalized_velocity_profile_800_ms.csv')
CBF_covid = pd.read_csv('zygote/csv_files/normalized_velocity_profile_700_ms.csv')
CBF_stress = pd.read_csv('zygote/csv_files/normalized_velocity_profile_650_ms.csv')

plt.figure(figsize=(8,2), constrained_layout=True)
# plt.suptitle(title, fontsize=40, fontweight="bold")

# [5%, 44%, 70%]

# at rest [0.08, 0.352, 0.56]
# ax1 = plt.subplot2grid(shape=(8), loc=(0,0))
plt.plot(CBF_at_rest.t, CBF_at_rest.vel * 2, '-k', label='CBF')
plt.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.08].t, CBF_at_rest[CBF_at_rest["t"] == 0.08].vel * 2, marker="o", edgecolors="black", color="blue", zorder=2) # t = 0.04 (5%)
plt.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.352].t, CBF_at_rest[CBF_at_rest["t"] == 0.352].vel * 2, marker="o", edgecolors="black", color="red", zorder=2) # t = 0.04 (5%)
plt.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.56].t, CBF_at_rest[CBF_at_rest["t"] == 0.56].vel * 2, marker="o", edgecolors="black", color="green", zorder=2) # t = 0.04 (5%)
plt.xlabel(r'Time [s]'), plt.ylabel(r'$\Psi_{CBF}$ [cm$^3$ / s]')
plt.title(r'Patient at rest (HR: 75 bpm)')
plt.xlim([0, 2.8]), plt.ylim([-1, 2*2.12])
# ax1.xaxis.set_major_formatter(formatter)
# plt.subplots_adjust(hspace=0.5)
plt.xticks(np.arange(0, 3.2, 0.4))
# for ax in [ax1, ax2]:
#     plt.setp(ax.get_xticklabels(), visible=False)
#     # The y-ticks will overlap with "hspace=0", so we'll hide the bottom tick
#     ax.set_yticks(ax.get_yticks()[1:])

# ax1.legend(), ax2.legend(), ax3.legend()

plt.savefig("Plots/CBF/CBF_ex_sum.pdf", transparent=True)

#########################################
# SINGLE CBF POINTS
#########################################
plt.figure(figsize=(4,4), constrained_layout=True)
ax1 = plt.subplot2grid(shape=(1,1), loc=(0,0))
ax1.plot(CBF_at_rest.t, CBF_at_rest.vel, '-k', linewidth=4)
ax1.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.08].t, CBF_at_rest[CBF_at_rest["t"] == 0.08].vel, s=240, marker="o", edgecolors="black", color="blue", zorder=2) # t = 0.04 (5%)
ax1.set_xlim([0, 0.8]), ax1.set_ylim([-1, 2.12])
plt.axis('off')
plt.savefig("Plots/CBF/CBF_1.png", transparent=True)

plt.figure(figsize=(4,4), constrained_layout=True)
ax1 = plt.subplot2grid(shape=(1,1), loc=(0,0))
ax1.plot(CBF_at_rest.t, CBF_at_rest.vel, '-k', linewidth=4)
ax1.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.352].t, CBF_at_rest[CBF_at_rest["t"] == 0.352].vel, s=240, marker="o", edgecolors="black", color="red", zorder=2) # t = 0.04 (5%)
ax1.set_xlim([0, 0.8]), ax1.set_ylim([-1, 2.12])
plt.axis('off')
plt.savefig("Plots/CBF/CBF_2.png", transparent=True)

plt.figure(figsize=(4,4), constrained_layout=True)
ax1 = plt.subplot2grid(shape=(1,1), loc=(0,0))
ax1.plot(CBF_at_rest.t, CBF_at_rest.vel, '-k', linewidth=4)
ax1.scatter(CBF_at_rest[CBF_at_rest["t"] == 0.56].t, CBF_at_rest[CBF_at_rest["t"] == 0.56].vel, s=240, marker="o", edgecolors="black", color="green", zorder=2) # t = 0.04 (5%)
ax1.set_xlim([0, 0.8]), ax1.set_ylim([-1, 2.12])
plt.axis('off')
plt.savefig("Plots/CBF/CBF_3.png", transparent=True)

#########################################
# SIMULATIONS
#########################################
mpl.rcParams.update({'font.size': 22})

app_0d_complete = pd.read_csv('Results/oxygen_exchange_0d_complete/oxygen_exchange.csv')
app_0d_reduced = pd.read_csv('Results/oxygen_exchange_0d_reduced/oxygen_exchange.csv')
app_3d = pd.read_csv('Results/oxygen_exchange_3d/oxygen_exchange.csv')
perfusion_oe = pd.read_csv('Results/perfusion_oxygen_exchange/perfusion.csv')
perfusion_cor = pd.read_csv('Results/perfusion_3d_coronaries/perfusion.csv')
perfusion_heart = pd.read_csv('Results/perfusion_heart/perfusion.csv')
perfusion_heart_covid = pd.read_csv('Results/perfusion_heart_covid/perfusion.csv')
perfusion_heart_stress = pd.read_csv('Results/perfusion_heart_stress/perfusion.csv')
perfusion_heart_stress_covid = pd.read_csv('Results/perfusion_heart_stress_covid/perfusion.csv')

def plot(title, df, period, label, space, real, ref, marker, marker_color, filename, extension):
    if not os.path.exists("Plots"):
        os.makedirs("Plots")

    plt.figure(figsize=(20,30), constrained_layout=True)
    # plt.suptitle(title, fontsize=40, fontweight="bold")

    # SO2
    ax1 = plt.subplot2grid(shape=(3,4), loc=(0,2), colspan=2)
    ax1.set_title(r'SO$_2^3$'), ax1.set_xlabel(r'Time [s]'), ax1.set_ylabel('[$\%$]')
    ax1.set_xlim([0, 2.4]), ax1.set_ylim([50 , 100])
    # PO2 & POm
    ax2 = plt.subplot2grid((3,4), (0,0), colspan=2)
    ax2.set_title(r'PO$_2^3$ and PO$_2^m$'), ax2.set_xlabel(r'Time [s]'), ax2.set_ylabel('Pressure [mmHg]')
    ax2.set_xlim([0, 2.4]), ax2.set_ylim([0, 120])
    # c_O2_star
    ax3 = plt.subplot2grid((3,4), (1,0), colspan=2)
    ax3.set_title(r'[O$_2^*$]$^3$'), ax3.set_xlabel(r'Time [s]'), ax3.set_ylabel('Concentration [mol m$^{-3}$]')
    ax3.set_xlim([0, 2.4]), ax3.set_ylim([15, 30])
    # O2 fluxes
    ax4 = plt.subplot2grid((3,4), (1,2), colspan=2)
    ax4.set_title(r'$\lambda_{\mathrm{O}_2}^{\mathrm{del}}$ and $\lambda_{\mathrm{O}_2}^{\mathrm{cons}}$'), ax4.set_xlabel(r'Time [s]'), ax4.set_ylabel('Flux [$\mu$ mol / L / s]')
    ax4.set_xlim([0, 2.4]), ax4.set_ylim([0, 90])
    # O2 released
    ax5 = plt.subplot2grid((3,4), (2,1), colspan=2)
    ax5.set_title(r'$\Lambda_{\mathrm{O}_2}^{\mathrm{del}}$ and $\Lambda_{\mathrm{O}_2}^{\mathrm{cons}}}$'), ax5.set_xlabel(r'Time [s]'), ax5.set_ylabel('Flux [mol / L]')
    ax5.set_xlim([0, 2.4]), ax5.set_ylim([0, 150])

    kwargs = []
    kwargs.append({})
    kwargs.append({})
    if not real[1]:
        kwargs[1] = {"linestyle": "None", "marker": "x", "markersize": 6, "markevery": 2}
    else:
        kwargs[1] = {"linestyle": "dashed"}

    for i in range(2):
        # SO2
        ax1.plot(df[i]["time"] - period[i], df[i]["SO_2" + ("_avg" if space[i] else "")], color="C0", label=label[i] + (" (avg)" if space[i] else "") , **kwargs[i])
        # PO2 & POm
        ax2.plot(df[i]["time"] - period[i], df[i]["PO_2" + ("_avg" if space[i] else "")], color="C0", label=label[i] + ', capillaries' + (" (avg)" if space[i] else "") , **kwargs[i])
        ax2.plot(df[i]["time"] - period[i], df[i]["PO_2_muscle" + ("_avg" if space[i] else "")], color="C1", label=label[i] + ', muscle' + (" (avg)" if space[i] else "") , **kwargs[i])
        for j in range(len(ref)):
            ax2.axhline(y=ref[j], color="black", linestyle="dashed")
        # c_O2_star
        ax3.plot(df[i]["time"] - period[i], df[i]["O2_star" + ("_avg" if space[i] else "")], color="C0", label=label[i] + (" (avg)" if space[i] else ""), **kwargs[i])
        # O2 fluxes
        ax4.plot(df[i]["time"] - period[i], df[i]["flux_O2_blood_muscle"], color="C0", label=label[i] + r', $\lambda_{\mathrm{O}_2}^{\mathrm{del}}$', **kwargs[i])
        ax4.plot(df[i]["time"] - period[i], df[i]["flux_O2_muscle_ATP"], color="C1", label=label[i] + r', $\lambda_{\mathrm{O}_2}^{\mathrm{cons}}$', **kwargs[i])
        # O2 released
        ax5.plot(df[i]["time"] - period[i], df[i]["cumulative_O2_released"] - df[i].loc[df[i]["time"] == period[i],  "cumulative_O2_released"].iloc[0], color="C0", label=label[i] + r', $\Lambda_{\mathrm{O}_2}^{\mathrm{del}}$', **kwargs[i])
        ax5.plot(df[i]["time"] - period[i], df[i]["cumulative_O2_consumed"] - df[i].loc[df[i]["time"] == period[i], "cumulative_O2_consumed"].iloc[0], color="C1", label=label[i] + r', $\Lambda_{\mathrm{O}_2}^{\mathrm{cons}}$', **kwargs[i])

    # real geometry plots
    for i in range(2):
        if (real[i]):
            # SO2
            ax1.plot(df[i]["time"] - period[i], df[i]["SO_2_point"], color="C0", label=label[i] + ' (a point)', linestyle="dotted")
            ax1.fill_between(df[i]["time"] - period[i], df[i]["SO_2_min"], df[i]["SO_2_max"], color="C0", alpha=0.2)
            # PO2 & POm
            ax2.plot(df[i]["time"] - period[i], df[i]["PO_2_point"], color="C0", label=label[i] + ' (a point)', linestyle="dotted")
            ax2.fill_between(df[i]["time"] - period[i], df[i]["PO_2_min"], df[i]["PO_2_max"], color="C0", alpha=0.2)
            ax2.plot(df[i]["time"] - period[i], df[i]["PO_2_muscle_point"], color="C1", label=label[i] + ', muscle (a point)', linestyle="dotted")
            ax2.fill_between(df[i]["time"] - period[i], df[i]["PO_2_muscle_min"], df[i]["PO_2_muscle_max"], color="C1", alpha=0.2)
            # c_O2_star
            ax3.plot(df[i]["time"] - period[i], df[i]["O2_star_point"], color="C0", label=label[i] + ' (a point)', linestyle="dotted")
            ax3.fill_between(df[i]["time"] - period[i], df[i]["O2_star_min"], df[i]["O2_star_max"], color="C0", alpha=0.2)

    # scatter plots
    for i in range(2):
        if (real[i]):
            for j in range(len(marker_color)):
                # for k in range(3):
                k=0
                # SO2
                ax1.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(k*period[i] + period[i] + marker[i][j], 3)]["SO_2" + ("_avg" if space[i] else "")], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)
                # PO2 & POm
                ax2.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(k*period[i] + period[i] + marker[i][j], 3)]["PO_2" + ("_avg" if space[i] else "")], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)
                ax2.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(k*period[i] + period[i] + marker[i][j], 3)]["PO_2_muscle" + ("_avg" if space[i] else "")], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)
                # # # c_O2_star
                ax3.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(k*period[i] + period[i] + marker[i][j], 3)]["O2_star" + ("_avg" if space[i] else "")], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)
                # # O2 fluxes
                ax4.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["flux_O2_blood_muscle"], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)
                ax4.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["flux_O2_muscle_ATP"], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)
                # # # O2 released
                ax5.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["cumulative_O2_released"] - df[i].loc[df[i]["time"] == period[i], "cumulative_O2_released"].iloc[0], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)
                ax5.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["cumulative_O2_consumed"] - df[i].loc[df[i]["time"] == period[i], "cumulative_O2_consumed"].iloc[0], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)

    ax1.legend(prop={'size': 22}), ax2.legend(prop={'size': 22}, ncol=1), ax3.legend(prop={'size': 22}), ax4.legend(prop={'size': 22}), ax5.legend(prop={'size': 22})
    ax1.set_xticks(np.arange(0, 2.8, 0.4)), ax2.set_xticks(np.arange(0, 2.8, 0.4)), ax3.set_xticks(np.arange(0, 2.8, 0.4)), ax4.set_xticks(np.arange(0, 2.8, 0.4)), ax5.set_xticks(np.arange(0, 2.8, 0.4))
    # ax1.xaxis.set_major_formatter(formatter), ax2.xaxis.set_major_formatter(formatter), ax3.xaxis.set_major_formatter(formatter), ax4.xaxis.set_major_formatter(formatter), ax5.xaxis.set_major_formatter(formatter)
    # ax1.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2g'))
    labels = [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4]
    ax1.set_xticklabels(labels), ax2.set_xticklabels(labels), ax3.set_xticklabels(labels), ax4.set_xticklabels(labels), ax5.set_xticklabels(labels)

    kwargs = {}

    if extension == "png":
        kwargs["dpi"] = 300

    plt.savefig("Plots/comparisons/"+filename+"."+extension, **kwargs, transparent=True)

extension = "pdf"

plot("Comparison between reduced and complete model", [app_0d_complete, app_0d_reduced], [0.8, 0.8], ["complete", "reduced"], [False, False], [False, False], [40], [[],[]], [], "01_complete_reduced", extension)
plot("Comparison between 3D and 0D model", [app_0d_reduced, app_3d], [0.8, 0.8], ["0D", "3D"], [False, True], [False, False], [40], [[],[]], [], "02_3D_0D", extension)
plot("Comparison between semi-coupled and uncoupled model", [app_3d, perfusion_oe], [0.8, 0.8], ["uncoupled", "semi-coupled"], [True, True], [False, False], [40], [[],[]], [], "03_semicoupled_uncoupled", extension)
plot("Comparison between semi-coupled and coupled model", [perfusion_oe, perfusion_cor], [0.8, 0.8], ["direct flux", "coronaries"], [True, True], [False, False], [40],  [[],[]], [], "04_coronaries_direct_flux", extension)
plot("Comparison between real and ideal geometries", [perfusion_cor, perfusion_heart], [0.8, 0.8], ["ideal", "real"], [True, True], [False, True], [40], [[], [0.08, 0.352, 0.56]], ["blue", "red", "green"], "05_real_ideal", extension)
plot("Effect of physical activity on a healthy patient", [perfusion_heart, perfusion_heart_stress], [0.8, 0.65], ["at rest", "p. a."], [True, True], [True, True], [40, 20], [[0.08, 0.352, 0.56], [0.033, 0.286, 0.455]], ["blue", "red", "green"], "06_rest_stress", extension)
plot("Effect of Sars-CoV-2 disease", [perfusion_heart, perfusion_heart_covid], [0.8, 0.7], ["healthy", "Sars-CoV-2"], [True, True], [True, True], [40], [[0.08, 0.352, 0.56], [0.07, 0.308, 0.49]], ["blue", "red", "green"], "07_healthy_covid", extension)
plot("Effect of physical activity on a patient affected by Sars-CoV-2 disease", [perfusion_heart_covid, perfusion_heart_stress_covid], [0.7, 0.65], ["at rest", "p. a."], [True, True], [True, True], [40, 20], [[0.07, 0.308, 0.49], [0.033, 0.286, 0.455]], ["blue", "red", "green"], "08_rest_stress_covid", extension)

#########################################
# SIMULATIONS EXECUTIVE REPORT
#########################################
mpl.rcParams.update({'font.size': 22})

app_0d_complete = pd.read_csv('Results/oxygen_exchange_0d_complete/oxygen_exchange.csv')
app_0d_reduced = pd.read_csv('Results/oxygen_exchange_0d_reduced/oxygen_exchange.csv')
app_3d = pd.read_csv('Results/oxygen_exchange_3d/oxygen_exchange.csv')
perfusion_oe = pd.read_csv('Results/perfusion_oxygen_exchange/perfusion.csv')
perfusion_cor = pd.read_csv('Results/perfusion_3d_coronaries/perfusion.csv')
perfusion_heart = pd.read_csv('Results/perfusion_heart/perfusion.csv')
perfusion_heart_covid = pd.read_csv('Results/perfusion_heart_covid/perfusion.csv')
perfusion_heart_stress = pd.read_csv('Results/perfusion_heart_stress/perfusion.csv')
perfusion_heart_stress_covid = pd.read_csv('Results/perfusion_heart_stress_covid/perfusion.csv')

def plot(title, df, period, label, space, real, ref, marker, marker_color, filename, extension):
    if not os.path.exists("Plots"):
        os.makedirs("Plots")

    plt.figure(figsize=(16,8), constrained_layout=False)

    ax3 = plt.subplot2grid((1,2), (0,0))
    ax3.set_title(r'[O$_2^*$]$^3$'), ax3.set_xlabel(r'Time [s]'), ax3.set_ylabel('Concentration [mol m$^{-3}$]')
    ax3.set_xlim([0, 2.4]), ax3.set_ylim([15, 30])
    ax4 = plt.subplot2grid((1,2), (0,1))
    ax4.set_title(r'$\lambda_{\mathrm{O}_2}^{\mathrm{del}}$ and $\lambda_{\mathrm{O}_2}^{\mathrm{cons}}$'), ax4.set_xlabel(r'Time [s]'), ax4.set_ylabel('Flux [$\mu$ mol / L / s]')
    ax4.set_xlim([0, 2.4]), ax4.set_ylim([0, 90])

    kwargs = []
    kwargs.append({})
    kwargs.append({})
    if not real[1]:
        kwargs[1] = {"linestyle": "None", "marker": "x", "markersize": 6, "markevery": 2}
    else:
        kwargs[1] = {"linestyle": "dashed"}

    for i in range(2):
        ax3.plot(df[i]["time"] - period[i], df[i]["O2_star" + ("_avg" if space[i] else "")], color="C0", label=label[i] + (" (avg)" if space[i] else ""), **kwargs[i])
        ax4.plot(df[i]["time"] - period[i], df[i]["flux_O2_blood_muscle"], color="C0", label=label[i] + r', $\lambda_{\mathrm{O}_2}^{\mathrm{del}}$', **kwargs[i])
        ax4.plot(df[i]["time"] - period[i], df[i]["flux_O2_muscle_ATP"], color="C1", label=label[i] + r', $\lambda_{\mathrm{O}_2}^{\mathrm{cons}}$', **kwargs[i])

    # real geometry plots
    for i in range(2):
        if (real[i]):
            ax3.plot(df[i]["time"] - period[i], df[i]["O2_star_point"], color="C0", label=label[i] + ' (a point)', linestyle="dotted")
            ax3.fill_between(df[i]["time"] - period[i], df[i]["O2_star_min"], df[i]["O2_star_max"], color="C0", alpha=0.2)

    # scatter plots
    for i in range(2):
        if (real[i]):
            for j in range(len(marker_color)):
                k=0
                ax3.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(k*period[i] + period[i] + marker[i][j], 3)]["O2_star" + ("_avg" if space[i] else "")], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)
                ax4.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["flux_O2_blood_muscle"], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)
                ax4.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["flux_O2_muscle_ATP"], marker="o", edgecolors="black", s=120, color=marker_color[j], zorder=2)

    ax3.legend(prop={'size': 22}), ax4.legend(prop={'size': 22})
    ax3.set_xticks(np.arange(0, 2.8, 0.4)), ax4.set_xticks(np.arange(0, 2.8, 0.4))
    labels = [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4]
    ax3.set_xticklabels(labels), ax4.set_xticklabels(labels),

    kwargs = {}
    if extension == "png":
        kwargs["dpi"] = 300

    plt.savefig("Plots/comparisons/"+filename+"."+extension, **kwargs, transparent=True)

extension = "pdf"

# plot("Comparison between ivity on a healthy patient", [perfusion_heart, perfusion_heart_stress], [0.8, 0.65], ["at rest", "p. a."], [True, True], [True, True], [40, 20], [[0.08, 0.352, 0.56], [0.033, 0.286, 0.455]], ["blue", "red", "green"], "06_rest_stress", extension)
plot("Effect of Sars-CoV-2 disease", [perfusion_heart, perfusion_heart_covid], [0.8, 0.7], ["healthy", "Sars-CoV-2"], [True, True], [True, True], [40], [[0.08, 0.352, 0.56], [0.07, 0.308, 0.49]], ["blue", "red", "green"], "07_healthy_covid_ex_sum", extension)


#########################################
# OUTPUT OF 0D MODEL
#########################################

plt.figure(figsize=(20,30), constrained_layout=True)
# plt.suptitle(title, fontsize=40, fontweight="bold")

# SO2
ax1 = plt.subplot2grid(shape=(3,4), loc=(0,2), colspan=2)
ax1.set_title(r'SO$_2^3$'), ax1.set_xlabel(r'Time [s]'), ax1.set_ylabel('[$\%$]')
ax1.set_xlim([0, 2.4]), ax1.set_ylim([50 , 100])
# PO2 & POm
ax2 = plt.subplot2grid((3,4), (0,0), colspan=2)
ax2.set_title(r'PO$_2^3$ and PO$_2^m$'), ax2.set_xlabel(r'Time [s]'), ax2.set_ylabel('Pressure [mmHg]')
ax2.set_xlim([0, 2.4]), ax2.set_ylim([0, 120])
# c_O2_star
ax3 = plt.subplot2grid((3,4), (1,0), colspan=2)
ax3.set_title(r'[O$_2^*$]$^3$'), ax3.set_xlabel(r'Time [s]'), ax3.set_ylabel('Concentration [mol m$^{-3}$]')
ax3.set_xlim([0, 2.4]), ax3.set_ylim([15, 30])
# O2 fluxes
ax4 = plt.subplot2grid((3,4), (1,2), colspan=2)
ax4.set_title(r'$\lambda_{\mathrm{O}_2}^{\mathrm{del}}$ and $\lambda_{\mathrm{O}_2}^{\mathrm{cons}}$'), ax4.set_xlabel(r'Time [s]'), ax4.set_ylabel('Flux [$\mu$ mol / L / s]')
ax4.set_xlim([0, 2.4]), ax4.set_ylim([0, 90])
# O2 released
ax5 = plt.subplot2grid((3,4), (2,1), colspan=2)
ax5.set_title(r'$\Lambda_{\mathrm{O}_2}^{\mathrm{del}}$ and $\Lambda_{\mathrm{O}_2}^{\mathrm{cons}}}$'), ax5.set_xlabel(r'Time [s]'), ax5.set_ylabel('Flux [mol / L]')
ax5.set_xlim([0, 2.4]), ax5.set_ylim([0, 150])

# SO2
ax1.plot(app_0d_complete["time"] - 0.8, app_0d_complete["SO_2"], color="C0")
# PO2 & POm
ax2.plot(app_0d_complete["time"] - 0.8, app_0d_complete["PO_2"], color="C0", label='capillaries')
ax2.plot(app_0d_complete["time"] - 0.8, app_0d_complete["PO_2_muscle"], color="C1", label='muscle')
ax2.axhline(y=40, color="black", linestyle="dashed")
# c_O2_star
ax3.plot(app_0d_complete["time"] - 0.8, app_0d_complete["O2_star"], color="C0")
# O2 fluxes
ax4.plot(app_0d_complete["time"] - 0.8, app_0d_complete["flux_O2_blood_muscle"], color="C0", label=r'blood $\rightarrow$ muscle')
ax4.plot(app_0d_complete["time"] - 0.8, app_0d_complete["flux_O2_muscle_ATP"], color="C1", label=r'muscle $\rightarrow$ ATP')
# O2 released
ax5.plot(app_0d_complete["time"] - 0.8, app_0d_complete["cumulative_O2_released"] - app_0d_complete.loc[app_0d_complete["time"] == 0.8,  "cumulative_O2_released"].iloc[0], color="C0", label=r'blood $\rightarrow$ muscle')
ax5.plot(app_0d_complete["time"] - 0.8, app_0d_complete["cumulative_O2_consumed"] - app_0d_complete.loc[app_0d_complete["time"] == 0.8, "cumulative_O2_consumed"].iloc[0], color="C1", label=r'muscle $\rightarrow$ ATP')

# ax1.legend(prop={'size': 22})
ax2.legend(prop={'size': 22}, ncol=1)
# ax3.legend(prop={'size': 22})
ax4.legend(prop={'size': 22})
ax5.legend(prop={'size': 22})
ax1.set_xticks(np.arange(0, 2.8, 0.4)), ax2.set_xticks(np.arange(0, 2.8, 0.4)), ax3.set_xticks(np.arange(0, 2.8, 0.4)), ax4.set_xticks(np.arange(0, 2.8, 0.4)), ax5.set_xticks(np.arange(0, 2.8, 0.4))
# ax1.xaxis.set_major_formatter(formatter), ax2.xaxis.set_major_formatter(formatter), ax3.xaxis.set_major_formatter(formatter), ax4.xaxis.set_major_formatter(formatter), ax5.xaxis.set_major_formatter(formatter)
# ax1.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2g'))
labels = [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4]
ax1.set_xticklabels(labels), ax2.set_xticklabels(labels), ax3.set_xticklabels(labels), ax4.set_xticklabels(labels), ax5.set_xticklabels(labels)

# plt.savefig("Plots/0_0d_model_output.pdf", transparent=True)
plt.savefig("Plots/comparisons/"+"00_0d_model_output"+"."+extension, transparent=True)

#########################################
# OUTPUT OF 0D MODEL SLIDES
#########################################
mpl.rcParams.update({'font.size': 30})
plt.figure(figsize=(30,20), constrained_layout=True)
# plt.suptitle(title, fontsize=40, fontweight="bold")

# SO2
ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
ax1.set_title(r'SO$_2^3$'), ax1.set_xlabel(r'Time [s]'), ax1.set_ylabel('[$\%$]')
ax1.set_xlim([0, 2.4]), ax1.set_ylim([50 , 100])
# PO2 & POm
ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
ax2.set_title(r'PO$_2^3$ and PO$_2^m$'), ax2.set_xlabel(r'Time [s]'), ax2.set_ylabel('Pressure [mmHg]')
ax2.set_xlim([0, 2.4]), ax2.set_ylim([0, 60])
# c_O2_star
ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
ax3.set_title(r'[O$_2^*$]$^3$'), ax3.set_xlabel(r'Time [s]'), ax3.set_ylabel('Concentration [mol m$^{-3}$]')
ax3.set_xlim([0, 2.4]), ax3.set_ylim([0, 30])
# O2 fluxes
ax4 = plt.subplot2grid((2,6), (1,1), colspan=2)
ax4.set_title(r'$\lambda_{\mathrm{O}_2}^{\mathrm{del}}$ and $\lambda_{\mathrm{O}_2}^{\mathrm{cons}}$'), ax4.set_xlabel(r'Time [s]'), ax4.set_ylabel('Flux [$\mu$ mol / L / s]')
ax4.set_xlim([0, 2.4]), ax4.set_ylim([0, 90])
# O2 released
ax5 = plt.subplot2grid((2,6), (1,3), colspan=2)
ax5.set_title(r'$\Lambda_{\mathrm{O}_2}^{\mathrm{del}}$ and $\Lambda_{\mathrm{O}_2}^{\mathrm{cons}}}$'), ax5.set_xlabel(r'Time [s]'), ax5.set_ylabel('Flux [mol / L]')
ax5.set_xlim([0, 2.4]), ax5.set_ylim([0, 150])

# SO2
ax1.plot(app_0d_complete["time"] - 0.8, app_0d_complete["SO_2"], color="C0")
# PO2 & POm
ax2.plot(app_0d_complete["time"] - 0.8, app_0d_complete["PO_2"], color="C0", label='capillaries')
ax2.plot(app_0d_complete["time"] - 0.8, app_0d_complete["PO_2_muscle"], color="C1", label='muscle')
ax2.axhline(y=40, color="black", linestyle="dashed")
# c_O2_star
ax3.plot(app_0d_complete["time"] - 0.8, app_0d_complete["O2_star"], color="C0")
# O2 fluxes
ax4.plot(app_0d_complete["time"] - 0.8, app_0d_complete["flux_O2_blood_muscle"], color="C0", label=r'blood $\rightarrow$ muscle')
ax4.plot(app_0d_complete["time"] - 0.8, app_0d_complete["flux_O2_muscle_ATP"], color="C1", label=r'muscle $\rightarrow$ ATP')
# O2 released
ax5.plot(app_0d_complete["time"] - 0.8, app_0d_complete["cumulative_O2_released"] - app_0d_complete.loc[app_0d_complete["time"] == 0.8,  "cumulative_O2_released"].iloc[0], color="C0", label=r'blood $\rightarrow$ muscle')
ax5.plot(app_0d_complete["time"] - 0.8, app_0d_complete["cumulative_O2_consumed"] - app_0d_complete.loc[app_0d_complete["time"] == 0.8, "cumulative_O2_consumed"].iloc[0], color="C1", label=r'muscle $\rightarrow$ ATP')

# ax1.legend(prop={'size': 22})
ax2.legend(prop={'size': 30}, ncol=1)
# ax3.legend(prop={'size': 22})
ax4.legend(prop={'size': 30})
ax5.legend(prop={'size': 30})
ax1.set_xticks(np.arange(0, 2.8, 0.4)), ax2.set_xticks(np.arange(0, 2.8, 0.4)), ax3.set_xticks(np.arange(0, 2.8, 0.4)), ax4.set_xticks(np.arange(0, 2.8, 0.4)), ax5.set_xticks(np.arange(0, 2.8, 0.4))
# ax1.xaxis.set_major_formatter(formatter), ax2.xaxis.set_major_formatter(formatter), ax3.xaxis.set_major_formatter(formatter), ax4.xaxis.set_major_formatter(formatter), ax5.xaxis.set_major_formatter(formatter)
# ax1.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2g'))
labels = [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4]
ax1.set_xticklabels(labels), ax2.set_xticklabels(labels), ax3.set_xticklabels(labels), ax4.set_xticklabels(labels), ax5.set_xticklabels(labels)

# plt.savefig("Plots/0_0d_model_output.pdf", transparent=True)
plt.savefig("Plots/comparisons_slides/"+"00_0d_model_output"+"."+extension, transparent=True)

#########################################
# SIMULATIONS SLIDES
#########################################
mpl.rcParams.update({'font.size': 30})

app_0d_complete = pd.read_csv('Results/oxygen_exchange_0d_complete/oxygen_exchange.csv')
app_0d_reduced = pd.read_csv('Results/oxygen_exchange_0d_reduced/oxygen_exchange.csv')
app_3d = pd.read_csv('Results/oxygen_exchange_3d/oxygen_exchange.csv')
perfusion_oe = pd.read_csv('Results/perfusion_oxygen_exchange/perfusion.csv')
perfusion_cor = pd.read_csv('Results/perfusion_3d_coronaries/perfusion.csv')
perfusion_heart = pd.read_csv('Results/perfusion_heart/perfusion.csv')
perfusion_heart_covid = pd.read_csv('Results/perfusion_heart_covid/perfusion.csv')
perfusion_heart_stress = pd.read_csv('Results/perfusion_heart_stress/perfusion.csv')
perfusion_heart_stress_covid = pd.read_csv('Results/perfusion_heart_stress_covid/perfusion.csv')

def plot_slides(title, df, period, label, space, real, ref, marker, marker_color, filename, extension):
    if not os.path.exists("Plots"):
        os.makedirs("Plots")

    plt.figure(figsize=(30,20), constrained_layout=True)
    # plt.suptitle(title, fontsize=40, fontweight="bold")

    # SO2
    ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
    ax1.set_title(r'SO$_2^3$'), ax1.set_xlabel(r'Time [s]'), ax1.set_ylabel('[$\%$]')
    ax1.set_xlim([0, 2.4]), ax1.set_ylim([50 , 100])
    # PO2 & POm
    ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
    ax2.set_title(r'PO$_2^3$ and PO$_2^m$'), ax2.set_xlabel(r'Time [s]'), ax2.set_ylabel('Pressure [mmHg]')
    ax2.set_xlim([0, 2.4]), ax2.set_ylim([0, 60])
    # c_O2_star
    ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
    ax3.set_title(r'[O$_2^*$]$^3$'), ax3.set_xlabel(r'Time [s]'), ax3.set_ylabel('Concentration [mol m$^{-3}$]')
    ax3.set_xlim([0, 2.4]), ax3.set_ylim([0, 30])
    # O2 fluxes
    ax4 = plt.subplot2grid((2,6), (1,0), colspan=2) # 1,1
    ax4.set_title(r'$\lambda_{\mathrm{O}_2}^{\mathrm{del}}$ and $\lambda_{\mathrm{O}_2}^{\mathrm{cons}}$'), ax4.set_xlabel(r'Time [s]'), ax4.set_ylabel('Flux [$\mu$ mol / L / s]')
    ax4.set_xlim([0, 2.4]), ax4.set_ylim([0, 90])
    # O2 released
    ax5 = plt.subplot2grid((2,6), (1,2), colspan=2) #1,3
    ax5.set_title(r'$\Lambda_{\mathrm{O}_2}^{\mathrm{del}}$ and $\Lambda_{\mathrm{O}_2}^{\mathrm{cons}}}$'), ax5.set_xlabel(r'Time [s]'), ax5.set_ylabel('Flux [mol / L]')
    ax5.set_xlim([0, 2.4]), ax5.set_ylim([0, 150])

    kwargs = []
    kwargs.append({})
    kwargs.append({})
    if not real[1]:
        kwargs[1] = {"linestyle": "None", "marker": "x", "markersize": 6, "markevery": 2}
    else:
        kwargs[1] = {"linestyle": (0, (5, 10))}

    for i in range(2):
        # SO2
        ax1.plot(df[i]["time"] - period[i], df[i]["SO_2" + ("_avg" if space[i] else "")], color="C0", label=label[i] + (" (avg)" if space[i] else "") , **kwargs[i], linewidth=3)
        # PO2 & POm
        ax2.plot(df[i]["time"] - period[i], df[i]["PO_2" + ("_avg" if space[i] else "")], color="C0", label=label[i] + ', capillaries' + (" (avg)" if space[i] else "") , **kwargs[i], linewidth=3)
        ax2.plot(df[i]["time"] - period[i], df[i]["PO_2_muscle" + ("_avg" if space[i] else "")], color="C1", label=label[i] + ', muscle' + (" (avg)" if space[i] else "") , **kwargs[i], linewidth=3)
        for j in range(len(ref)):
            ax2.axhline(y=ref[j], color="black", linestyle="dotted")
        # c_O2_star
        ax3.plot(df[i]["time"] - period[i], df[i]["O2_star" + ("_avg" if space[i] else "")], color="C0", label=label[i] + (" (avg)" if space[i] else ""), **kwargs[i], linewidth=3)
        # O2 fluxes
        ax4.plot(df[i]["time"] - period[i], df[i]["flux_O2_blood_muscle"], color="C0", label=label[i] + r', $\lambda_{\mathrm{O}_2}^{\mathrm{del}}$', **kwargs[i], linewidth=3)
        ax4.plot(df[i]["time"] - period[i], df[i]["flux_O2_muscle_ATP"], color="C1", label=label[i] + r', $\lambda_{\mathrm{O}_2}^{\mathrm{cons}}$', **kwargs[i], linewidth=3)
        # O2 released
        ax5.plot(df[i]["time"] - period[i], df[i]["cumulative_O2_released"] - df[i].loc[df[i]["time"] == period[i],  "cumulative_O2_released"].iloc[0], color="C0", label=label[i] + r', $\Lambda_{\mathrm{O}_2}^{\mathrm{del}}$', **kwargs[i], linewidth=3)
        ax5.plot(df[i]["time"] - period[i], df[i]["cumulative_O2_consumed"] - df[i].loc[df[i]["time"] == period[i], "cumulative_O2_consumed"].iloc[0], color="C1", label=label[i] + r', $\Lambda_{\mathrm{O}_2}^{\mathrm{cons}}$', **kwargs[i], linewidth=3)

    # real geometry plots
    for i in range(2):
        if (real[i]):
            # SO2
            # ax1.plot(df[i]["time"] - period[i], df[i]["SO_2_point"], color="C0", linestyle="dotted")
            ax1.fill_between(df[i]["time"] - period[i], df[i]["SO_2_min"], df[i]["SO_2_max"], color="C0", alpha=0.2)
            # PO2 & POm
            # ax2.plot(df[i]["time"] - period[i], df[i]["PO_2_point"], color="C0", linestyle="dotted")
            ax2.fill_between(df[i]["time"] - period[i], df[i]["PO_2_min"], df[i]["PO_2_max"], color="C0", alpha=0.2)
            # ax2.plot(df[i]["time"] - period[i], df[i]["PO_2_muscle_point"], color="C1", linestyle="dotted")
            ax2.fill_between(df[i]["time"] - period[i], df[i]["PO_2_muscle_min"], df[i]["PO_2_muscle_max"], color="C1", alpha=0.2)
            # c_O2_star
            # ax3.plot(df[i]["time"] - period[i], df[i]["O2_star_point"], color="C0", linestyle="dotted")
            ax3.fill_between(df[i]["time"] - period[i], df[i]["O2_star_min"], df[i]["O2_star_max"], color="C0", alpha=0.2)

    # scatter plots
    for i in range(2):
        if (real[i]):
            for j in range(len(marker_color)):
                # for k in range(3):
                k=0
                # SO2
                ax1.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(k*period[i] + period[i] + marker[i][j], 3)]["SO_2" + ("_avg" if space[i] else "")], marker="o", edgecolors="black", s=240, color=marker_color[j], zorder=2)
                # PO2 & POm
                ax2.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(k*period[i] + period[i] + marker[i][j], 3)]["PO_2" + ("_avg" if space[i] else "")], marker="o", edgecolors="black", s=240, color=marker_color[j], zorder=2)
                ax2.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(k*period[i] + period[i] + marker[i][j], 3)]["PO_2_muscle" + ("_avg" if space[i] else "")], marker="o", edgecolors="black", s=240, color=marker_color[j], zorder=2)
                # # # c_O2_star
                ax3.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(k*period[i] + period[i] + marker[i][j], 3)]["O2_star" + ("_avg" if space[i] else "")], marker="o", edgecolors="black", s=240, color=marker_color[j], zorder=2)
                # # O2 fluxes
                ax4.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["flux_O2_blood_muscle"], marker="o", edgecolors="black", s=240, color=marker_color[j], zorder=2)
                ax4.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["flux_O2_muscle_ATP"], marker="o", edgecolors="black", s=240, color=marker_color[j], zorder=2)
                # # # O2 released
                ax5.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["cumulative_O2_released"] - df[i].loc[df[i]["time"] == period[i], "cumulative_O2_released"].iloc[0], marker="o", edgecolors="black", s=240, color=marker_color[j], zorder=2)
                ax5.scatter(df[i][df[i]["time"] == round(marker[i][j] + k*period[i], 3)].time, df[i][df[i]["time"] == round(1*period[i] + marker[i][j], 3)]["cumulative_O2_consumed"] - df[i].loc[df[i]["time"] == period[i], "cumulative_O2_consumed"].iloc[0], marker="o", edgecolors="black", s=240, color=marker_color[j], zorder=2)

    ax1.legend(prop={'size': 30}), ax2.legend(prop={'size': 30}, ncol=1), ax3.legend(prop={'size': 30}), ax4.legend(prop={'size': 30}), ax5.legend(prop={'size': 30})
    ax1.set_xticks(np.arange(0, 2.8, 0.4)), ax2.set_xticks(np.arange(0, 2.8, 0.4)), ax3.set_xticks(np.arange(0, 2.8, 0.4)), ax4.set_xticks(np.arange(0, 2.8, 0.4)), ax5.set_xticks(np.arange(0, 2.8, 0.4))
    # ax1.xaxis.set_major_formatter(formatter), ax2.xaxis.set_major_formatter(formatter), ax3.xaxis.set_major_formatter(formatter), ax4.xaxis.set_major_formatter(formatter), ax5.xaxis.set_major_formatter(formatter)
    # ax1.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2g'))
    labels = [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4]
    ax1.set_xticklabels(labels), ax2.set_xticklabels(labels), ax3.set_xticklabels(labels), ax4.set_xticklabels(labels), ax5.set_xticklabels(labels)

    kwargs = {}
    if extension == "png":
        kwargs["dpi"] = 300

    plt.savefig("Plots/comparisons_slides/"+filename+"."+extension, **kwargs, transparent=True)
    plt.savefig("Plots/comparisons_slides/"+filename+"."+"png", **kwargs, transparent=True)

extension = "pdf"

plot_slides("Comparison between reduced and complete model", [app_0d_complete, app_0d_reduced], [0.8, 0.8], ["complete", "reduced"], [False, False], [False, False], [40], [[],[]], [], "01_complete_reduced", extension)
plot_slides("Comparison between 3D and 0D model", [app_0d_reduced, app_3d], [0.8, 0.8], ["0D", "3D"], [False, True], [False, False], [40], [[],[]], [], "02_3D_0D", extension)
plot_slides("Comparison between semi-coupled and uncoupled model", [app_3d, perfusion_oe], [0.8, 0.8], ["uncoupled", "semi-coupled"], [True, True], [False, False], [40], [[],[]], [], "03_semicoupled_uncoupled", extension)
plot_slides("Comparison between semi-coupled and coupled model", [perfusion_oe, perfusion_cor], [0.8, 0.8], ["direct flux", "coronaries"], [True, True], [False, False], [40],  [[],[]], [], "04_coronaries_direct_flux", extension)
plot_slides("Comparison between real and ideal geometries", [perfusion_cor, perfusion_heart], [0.8, 0.8], ["ideal", "real"], [True, True], [False, True], [40], [[], [0.08, 0.352, 0.56]], ["blue", "red", "green"], "05_real_ideal", extension)
plot_slides("Effect of physical activity on a healthy patient", [perfusion_heart, perfusion_heart_stress], [0.8, 0.65], ["at rest", "p. a."], [True, True], [True, True], [40, 20], [[0.08, 0.352, 0.56], [0.033, 0.286, 0.455]], ["blue", "red", "green"], "06_rest_stress", extension)
plot_slides("Effect of Sars-CoV-2 disease", [perfusion_heart, perfusion_heart_covid], [0.8, 0.7], ["healthy", "Sars-CoV-2"], [True, True], [True, True], [40], [[0.08, 0.352, 0.56], [0.07, 0.308, 0.49]], ["blue", "red", "green"], "07_healthy_covid", extension)
plot_slides("Effect of physical activity on a patient affected by Sars-CoV-2 disease", [perfusion_heart_covid, perfusion_heart_stress_covid], [0.7, 0.65], ["at rest", "p. a."], [True, True], [True, True], [40, 20], [[0.07, 0.308, 0.49], [0.033, 0.286, 0.455]], ["blue", "red", "green"], "08_rest_stress_covid", extension)
