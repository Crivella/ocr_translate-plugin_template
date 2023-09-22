###################################################################################
# {{cookiecutter.plugin_name}} - a google_translate plugin for ocr_translate              #
# Copyright (C) 2023-present {{ cookiecutter.github_user }}                                      #
#                                                                                 #
# This program is free software: you can redistribute it and/or modify            #
# it under the terms of the GNU General Public License as published by            #
# the Free Software Foundation, either version 3 of the License.                  #
#                                                                                 #
# This program is distributed in the hope that it will be useful,                 #
# but WITHOUT ANY WARRANTY; without even the implied warranty of                  #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                   #
# GNU General Public License for more details.                                    #
#                                                                                 #
# You should have received a copy of the GNU General Public License               #
# along with this program.  If not, see {http://www.gnu.org/licenses/}.           #
#                                                                                 #
# Home: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}                          #
###################################################################################
"""{{ cookiecutter.short_description }}"""

from ocr_translate import models as m

from PIL import Image

class {{ cookiecutter.model_name_prefix | replace('_', '') }}OCRBoxModel(m.OCRBoxModel):
    """OCRBoxtranslate plugin to allow usage of ... for box detection."""
    class Meta:
        proxy = True

    def load(self):
        """Load the model into memory."""
        # Do something here to load the model or nothing if not needed (should still be defined)

    def unload(self) -> None:
        """Unload the model from memory."""
        # Do something here to unload the model or nothing if not needed (should still be defined)


    def _box_detection(
            self,
            image: Image.Image, options: dict = None
            ) -> list[tuple[int, int, int, int]]:
        """Perform box OCR on an image.

        Args:
            image (Image.Image): A Pillow image on which to perform OCR.
            options (dict, optional): A dictionary of options.

        Raises:
            NotImplementedError: The type of model specified is not implemented.

        Returns:
            list[tuple[int, int, int, int]]: A list of bounding boxes in lrbt format.
        """
        # Redefine this method with the same signature as above
        # Should return a list of `lrbt` boxes after processing the input PILImage

class {{ cookiecutter.model_name_prefix | replace('_', '') }}OCRModel(m.OCRModel):
    """OCRBoxtranslate plugin to allow usage of ... for box detection."""
    class Meta:
        proxy = True

    def load(self):
        """Load the model into memory."""
        # Do something here to load the model or nothing if not needed (should still be defined)

    def unload(self) -> None:
        """Unload the model from memory."""
        # Do something here to unload the model or nothing if not needed (should still be defined)


    def _ocr(
            self,
            img: Image.Image, lang: str = None, options: dict = None
            ) -> str:
        """Perform OCR on an image.

        Args:
            img (Image.Image):  A Pillow image on which to perform OCR.
            lang (str, optional): The language to use for OCR. (Not every model will use this)
            bbox (tuple[int, int, int, int], optional): The bounding box of the text on the image in lbrt format.
            options (dict, optional): A dictionary of options to pass to the OCR model.

        Raises:
            TypeError: If img is not a Pillow image.

        Returns:
            str: The text extracted from the image.
        """
        # Redefine this method with the same signature as above
        # Should return a sring with the result of the OCR performed on the input PILImage.
        # Unless the methods `prepare_image` or `ocr` are also being overwritten, the input image will be the result of the CROP on the original image using the bounding boxes given by the box detection model.

class {{ cookiecutter.model_name_prefix | replace('_', '') }}TSLModel(m.TSLModel):
    """OCRBoxtranslate plugin to allow usage of ... for box detection."""
    class Meta:
        proxy = True

    def load(self):
        """Load the model into memory."""
        # Do something here to load the model or nothing if not needed (should still be defined)

    def unload(self) -> None:
        """Unload the model from memory."""
        # Do something here to unload the model or nothing if not needed (should still be defined)


    def _translate(
            self,
            tokens: list, src_lang: str, dst_lang: str, options: dict = None) -> str | list[str]:
        """Translate a text using a the loaded model.

        Args:
            tokens (list): list or list[list] of string tokens to be translated.
            lang_src (str): Source language.
            lang_dst (str): Destination language.
            options (dict, optional): Options for the translation. Defaults to {}.

        Raises:
            TypeError: If text is not a string or a list of strings.

        Returns:
            Union[str,list[str]]: Translated text. If text is a list, returns a list of translated strings.
        """
        # Redefine this method with the same signature as above
        # Should return a sring with the translated text.
        # IMPORTANT: the main codebase treats this function as batchable:
        # The input `tokens` can be a list of strings or a list of list of strings. The output should match the input being a string or list of strings.
        # (This is used to leverage the capability of pytorch to batch inputs and outputs for faster performances, or it can also used to write a plugin for an online service by using a single request for multiple inputs using some separator that the service will leave unaltered.)
