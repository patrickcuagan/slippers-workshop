from wagtail import blocks
from wagtail.contrib.table_block.blocks import TableBlock as WagtailTableBlock
from wagtail.contrib.typed_table_block.blocks import (
    TypedTableBlock as WagtailTypedTableBlock,
)
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from ..constants import GROUP_CALLOUTS, GROUP_MEDIA, GROUP_TABLES, GROUP_TEXT


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        label="Image"
        icon = "image"
        group = GROUP_MEDIA
        template = "components/streamfield/image_block.html"


class DocumentBlock(blocks.StructBlock):
    document = DocumentChooserBlock()
    title = blocks.CharBlock(required=False)

    class Meta:
        label="Document"
        icon = "doc-full-inverse"
        group = GROUP_MEDIA
        template = "components/streamfield/document_block.html"


class TableBlock(WagtailTableBlock):
    class Meta:
        label="Simple table"
        group = GROUP_TABLES
        template = "components/streamfield/table_block.html"


class TypedTableBlock(blocks.StructBlock):
    caption = blocks.CharBlock(required=False)
    table = WagtailTypedTableBlock(
        [
            ("numeric", blocks.FloatBlock()),
            (
                "rich_text",
                blocks.RichTextBlock(
                    features=["bold", "italic", "link", "ol", "ul", "document-link"]
                ),
            ),
        ]
    )

    class Meta:
        label="Rich text and numeric table"
        icon = "table"
        group = GROUP_TABLES
        template = "components/streamfield/typed_table_block.html"


class QuoteBlock(blocks.StructBlock):
    quote = blocks.CharBlock(form_classname="title")
    attribution = blocks.CharBlock(required=False)

    class Meta:
        label="Quote"
        icon = "openquote"
        group = GROUP_TEXT
        template = "components/streamfield/quote_block.html"


class StoryBlock(blocks.StreamBlock):
    """
    Main StreamField block to be inherited by Pages
    """

    heading = blocks.CharBlock(
        form_classname="title",
        label="Heading",
        icon="title",
        group = GROUP_TEXT,
        template="components/streamfield/heading_block.html",
    )
    paragraph = blocks.RichTextBlock(
        label="Rich text",
        group = GROUP_TEXT,
    )
    image = ImageBlock()
    quote = QuoteBlock()
    embed = EmbedBlock(
        label="Embed",
        group=GROUP_MEDIA,
    )
    call_to_action = SnippetChooserBlock(
        "core.CallToActionSnippet",
        label="Call To Action",
        group=GROUP_CALLOUTS,
        template="components/streamfield/call_to_action_block.html",
    )
    document = DocumentBlock()
    table = TableBlock()
    typed_table = TypedTableBlock()

    class Meta:
        template = "components/streamfield/stream_block.html"
