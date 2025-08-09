from statsmodels.stats.proportion import proportions_ztest

def perform_z_test(successes, samples, alpha=0.05):
    """Run a two-proportion z-test and return results."""
    z_stat, p_val = proportions_ztest(successes, samples)
    conclusion = "Reject H₀" if p_val < alpha else "Fail to reject H₀"
    return z_stat, p_val, conclusion
