from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)


def main():
    # OpenAIのモデルのインスタンスを作成
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # プロンプトのテンプレート文章を定義
    template = """
    次の文章に誤字がないか調べて。誤字があれば訂正してください。
    {sentences_before_check}
    """

    # テンプレート文章にあるチェック対象の単語を変数化
    prompt = PromptTemplate(
    input_variables=["sentences_before_check"],
    template=template,
    )

    # OpenAIのAPIにこのプロンプトを送信するためのチェーンを作成
    chain = LLMChain(llm=chat, prompt=prompt,verbose=True)

    # チェーンを実行し、結果を表示
    print(chain("こんんんちわ、真純です。")['text'])


if __name__ == '__main__':
    main()