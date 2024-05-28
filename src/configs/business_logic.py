class BusinessLogicConfig:

    @staticmethod
    def get_system_message(system: str | None = None) -> str | None:
        """
        Get system message. If system is not provided, it will get the default system message.

        Args:
            system (str): System description.

        Returns:
            str: System message.
        """
        try:
            return system or open('src/data/system-message.txt', 'r').read()
        except FileNotFoundError:
            return None
