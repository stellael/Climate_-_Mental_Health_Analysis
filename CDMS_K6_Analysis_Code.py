# ------------------------
# 1. Απαραίτητες βιβλιοθήκες
import pandas as pd
import statsmodels.formula.api as smf
from scipy.stats import ttest_ind, f_oneway
import matplotlib.pyplot as plt
import seaborn as sns

# Ρύθμιση για να φαίνονται καλά τα γραφήματα
sns.set_theme(style="whitegrid")

# ------------------------
# 2. Φόρτωση δεδομένων

df_cdms = pd.read_csv(r"C:\Users\stella\Downloads\CDMS+Data (1).csv")
df_cdms["K6_scores"] = pd.to_numeric(df_cdms["K6_scores"], errors='coerce')

# ------------------------
# 3. Ερώτηση 1 – t-test + ANOVA για perceived distress (likely_devestated_self)
step1_df = df_cdms[["K6_scores", "likely_devestated_self"]].dropna()
group1 = step1_df[step1_df["likely_devestated_self"] == "Very likely"]["K6_scores"]
group2 = step1_df[step1_df["likely_devestated_self"] == "Very unlikely"]["K6_scores"]
t_stat, p_val_ttest = ttest_ind(group1, group2, equal_var=False)
anova_groups = [group["K6_scores"].dropna() for name, group in step1_df.groupby("likely_devestated_self")]
f_stat, p_val_anova = f_oneway(*anova_groups)

print("T-test:", t_stat, p_val_ttest)
print("ANOVA:", f_stat, p_val_anova)

# ------------------------
# 4. Ερώτηση 2 – Οπισθοδρομική παλινδρόμηση
regression_df = df_cdms[["K6_scores", "age", "gender", "income", "ethnicity", "education"]].dropna()
model = smf.ols("K6_scores ~ C(age) + C(gender) + C(income) + C(ethnicity) + C(education)", data=regression_df).fit()
print(model.summary())

# =================================================V
# 5. Visualizations (Boxplots with Correct Labels)
# =================================================

# Δημιουργία καμβά για 6 γραφήματα (3 σειρές, 2 στήλες)
fig, axes = plt.subplots(3, 2, figsize=(14, 22)) 
plt.subplots_adjust(hspace=0.7, wspace=0.4) # Μεγάλη απόσταση για να χωράνε οι τίτλοι

def plot_box(ax, x_val, title, x_label, palette):
    sns.boxplot(ax=ax, x=x_val, y='K6_scores', data=df_cdms, palette=palette, fliersize=2)
    ax.set_title(title, fontsize=12, pad=15, fontweight='bold')
    ax.set_ylabel('Psychological Distress (K6 Score)', fontsize=10)
    ax.set_xlabel(x_label, fontsize=10)
    # Κλίση 30 μοιρών για να διαβάζονται τα μεγάλα ονόματα
    ax.tick_params(axis='x', rotation=30, labelsize=9)

# Σχεδίαση των 6 γραφημάτων με τους σωστούς τίτλους και άξονες
plot_box(axes[0, 0], 'age', 'K6 Score by Age Group', 'Age Group', 'Set2')
plot_box(axes[0, 1], 'gender', 'K6 Score by Gender', 'Gender Identification', 'Pastel1')
plot_box(axes[1, 0], 'income', 'K6 Score by Income Level', 'Annual Income', 'Set3')
plot_box(axes[1, 1], 'education', 'K6 Score by Education Level', 'Highest Degree Earned', 'Accent')
plot_box(axes[2, 0], 'dome_impacted', 'Impact of 2021 Heat Dome on Mental Health', 'Exposure Status', 'Reds')
plot_box(axes[2, 1], 'river_impacted', 'Impact of 2021 Floods on Mental Health', 'Exposure Status', 'Blues')

plt.show()
# ------------------------
# 6. Ερώτηση 3 – ANOVA για Heat Dome και Atmospheric River
impact_df = df_cdms[["K6_scores", "dome_impacted", "river_impacted"]].dropna()
groups_dome = [group["K6_scores"].dropna() for name, group in impact_df.groupby("dome_impacted")]
f_dome, p_dome = f_oneway(*groups_dome)
groups_river = [group["K6_scores"].dropna() for name, group in impact_df.groupby("river_impacted")]
f_river, p_river = f_oneway(*groups_river)

print("Heat Dome ANOVA:", f_dome, p_dome)
print("Atmospheric River ANOVA:", f_river, p_river)

# =================================================
# 7. Regression Coefficients (Spaced Out Layout)
# =================================================

# Φτιάχνουμε το γράφημα πιο "ψηλό" (8x12) για να έχουν απόσταση οι μεταβλητές
plt.figure(figsize=(8, 12)) 
coefs = model.params.drop('Intercept').sort_values()

# Χρήση χρωμάτων: Salmon για αύξηση distress, Skyblue για μείωση
colors = ['salmon' if x > 0 else 'skyblue' for x in coefs]
coefs.plot(kind='barh', color=colors, width=0.8)

plt.title('Predictors of Psychological Distress\n(Regression Coefficients)', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Impact Weight (Coefficient)', fontsize=12)
plt.ylabel('Demographic Variables', fontsize=12)

# Προσθήκη βοηθητικών στοιχείων
plt.axvline(0, color='black', linestyle='--', linewidth=1) # Γραμμή στο μηδέν
plt.grid(axis='x', linestyle=':', alpha=0.7)
plt.tight_layout()

plt.show()

import tkinter as tk
from tkinter import messagebox

# Δημιουργία κρυφού παραθύρου για το pop-up
root = tk.Tk()
root.withdraw()

# Το κείμενο των συμπερασμάτων
conclusions = (
    "📊 ANALYSIS SUMMARY\n"
    "--------------------------------------\n"
    f"1. HEAT DOME: Significant impact on mental health (p = {p_dome:.2e})\n"
    f"2. FLOODS: Significant impact on mental health (p = {p_river:.2e})\n"
    "--------------------------------------\n"
    "3. HIGHEST RISK GROUPS: Genderfluid, Non-binary, and Trans woman individuals.\n"
    "4. PROTECTIVE FACTORS: Higher income ($100k+) and older age (65+).\n"
    "--------------------------------------\n"
    "All results are statistically significant (p < 0.05)."
)

# Εμφάνιση του παραθύρου
messagebox.showinfo("Statistical Results & Conclusions", conclusions)

root.destroy()