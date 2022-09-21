from src.Visualization import Vizualization


class MainSolution:
    """
    Take home test solution
    """
    def __init__(self):
        self.viz = Vizualization()

    def create_viz(self):
        print("HISTORICAL TABLE ACCOUNTS\n")
        self.viz.create_historical_table_accounts()
        print("\nHISTORICAL TABLE CARDS\n")
        self.viz.create_historical_table_cards()
        print("\nHISTORICAL TABLE SAVING ACCOUNTS\n")
        self.viz.create_historical_table_saving_accounts()
        print("\nDENORMALIZED HISTORICAL TABLE\n")
        self.viz.denormalized_historical_table()
        print("\nTRANSACTION ANALYSIS\n")
        self.viz.transaction_analysis()


if __name__ == "__main__":
    solution = MainSolution()
    solution.create_viz()


