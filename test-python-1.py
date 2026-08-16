# Fichier Python - Itachi99-cpu
def calculate_average(numbers):
    """Calcule la moyenne d'une liste de nombres"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Test de la fonction
test_scores = [15, 18, 12, 16, 14]
average = calculate_average(test_scores)
print(f"Moyenne des scores: {average}")
