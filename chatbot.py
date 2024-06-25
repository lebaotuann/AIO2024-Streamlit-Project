import streamlit as st
from hugchat import hugchat
from hugchat.login import Login


class Chatbot:

    @staticmethod
    def generate_response(prompt_input, email, password):
        """Generates LLM response

        Args:
            prompt_input (str):
            email (str): The email to login Hugging Face.
            password (str): The password.

        Returns:
            str: The response from the chatbot.
        """
        # Hugging Face Login
        sign = Login(email, password)
        cookies = sign.login()
        # Create ChatBot
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        return chatbot.chat(prompt_input)

    def run(self):
        """Run chatbot"""
        # App title
        st.title("Simple ChatBot")

        # Hugging Face Credentials
        with st.sidebar:
            st.title("Login HugChat")
            hf_email = st.text_input("Enter E-mail:")
            hf_pass = st.text_input("Enter Password: ", type="password")
            if not (hf_email and hf_pass):
                st.warning("Please enter your account!")
            else:
                st.success("Proceed to entering your prompt message!")

        # Store LLM generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [
                {"role": "assistant", "content": "How may I help you?"}
            ]

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # User-provided prompt
        if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

        # Generate a new response if last message is not from assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = self.generate_response(prompt, hf_email, hf_pass)
                    st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)


if __name__ == "__main__":
    Chatbot().run()
