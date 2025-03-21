from langchain_core.messages import trim_messages


class TrimmerManager:
    def __init__(self,
                 token_counter,
                 max_tokens:int=100,
                 strategy:str="last",
                 include_system:bool=True,
                 allow_partial:bool=False,
                 start_on:str="human"):
        """
        Initializes the trimming configuration.

        Args:
            token_counter: LLM instance for token counting.
            max_tokens (int): Maximum number of tokens to retain.
            strategy (str): Trimming strategy, e.g., "last".
            include_system (bool): Whether to include system messages.
            allow_partial (bool): Whether to allow partial messages.
            start_on (str): Where trimming starts, e.g., "human".
        """
        if token_counter is None:
            raise ValueError("LLM Model for Token counter is required.")

        self.trimmer = trim_messages(
            token_counter=token_counter,
            max_tokens=max_tokens,
            strategy=strategy,
            include_system=include_system,
            allow_partial=allow_partial,
            start_on=start_on
        )

    def trim(self, messages: list):
        """
        Invokes the trimmer on the given messages.

        Args:
            messages (list): The list of messages to trim.

        Returns:
            list: Trimmed messages.
        """
        return self.trimmer.invoke(messages)
