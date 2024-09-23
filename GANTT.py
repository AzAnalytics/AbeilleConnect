import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Définition des tâches avec leur durée (en jours)
tasks = {
    "Recherche et Planification": 14,
    "Conception Technique et Design": 15,
    "Développement Backend": 18,
    "Développement Application Mobile": 20,
    "Développement Application Web": 20,
    "Intégration Alertes et Notifications": 4,
    "Tests et Validation": 14,
    "Sécurité, Déploiement et Conformité": 12,
    "Marketing et Lancement": 15
}

# Date de début (demain)
start_date = datetime.now() + timedelta(days=1)


# Calcul de la date de fin en excluant les weekends
def calculate_end_date(start, duration):
    current = start
    while duration > 0:
        current += timedelta(days=1)
        if current.weekday() < 5:  # Lundi à vendredi
            duration -= 1
    return current


# Création d'un DataFrame avec les tâches, dates de début et de fin
task_names = []
start_dates = []
end_dates = []
current_start = start_date

for task, duration in tasks.items():
    task_names.append(task)
    start_dates.append(current_start)
    end_date = calculate_end_date(current_start, duration)
    end_dates.append(end_date)
    current_start = end_date + timedelta(days=1)

df = pd.DataFrame({
    "Task": task_names,
    "Start": start_dates,
    "End": end_dates
})

# Tracer le diagramme de Gantt
fig, ax = plt.subplots(figsize=(10, 6))

# Convertir les dates au format de matplotlib
start_dates_mpl = mdates.date2num(df["Start"])
end_dates_mpl = mdates.date2num(df["End"])

# Tracer chaque tâche comme une barre horizontale
for i, task in enumerate(reversed(df["Task"])):
    ax.barh(i, end_dates_mpl[len(df["Task"]) - 1 - i] - start_dates_mpl[len(df["Task"]) - 1 - i],
            left=start_dates_mpl[len(df["Task"]) - 1 - i], height=0.4, align='center')

# Formater le diagramme
ax.set_yticks(range(len(df["Task"])))
ax.set_yticklabels(reversed(df["Task"]))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
plt.xticks(rotation=45)
plt.title("Diagramme de Gantt pour le projet AbeilleConnect")
plt.xlabel("Date")
plt.ylabel("Tâches")
plt.grid(True)

# Afficher le diagramme
plt.tight_layout()
plt.show()

# Sauvegarder le diagramme
plt.savefig('gantt_chart_abeilleconnect.png')
