def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    num = len(set(recommended[:k]) & set(relevant))
    print(num)
    pres_k = num/k
    recall_k = num/len(relevant)
    return [pres_k, recall_k]