from enum import StrEnum


class AnthropicConstant:
    class ImageBlock:
        class MediaType(StrEnum):
            JPEG = "image/jpeg"
            PNG = "image/png"
            GIF = "image/gif"
            WEBP = "image/webp"

        class DataFormat(StrEnum):
            BASE64 = "base64"

        class Type(StrEnum):
            IMAGE = "image"

    class TextBlock:
        class Type(StrEnum):
            TEXT = "text"

    class Role(StrEnum):
        USER = "user"
        ASSISTANT = "assistant"

    class StopReason(StrEnum):
        END_TURN = "end_turn"
        MAX_TOKENS = "max_tokens"
        STOP_SEQUENCE = "stop_sequence"

    class Type(StrEnum):
        MESSAGE = "message"

    class Model(StrEnum):
        CLAUDE_3_OPUS_20240229 = "claude-3-opus-20240229"
        CLAUDE_3_SONNET_20240229 = "claude-3-sonnet-20240229"
        CLAUDE_3_HAIKU_20240307 = "claude-3-haiku-20240307"
        CLAUDE_2_1 = "claude-2.1"
        CLAUDE_2_0 = "claude-2.0"
        CLAUDE_INSTANT_1_2 = "claude-instant-1.2"