from image_feature_extractor import ImageFeatureExtractor
from shadow_creator import ShadowCreator
from shadow_exporter import ShadowExporter
from shader_modifier import ShaderModifier
from shadow_optimizer import ShadowOptimizer

class QuickShador:
    def __init__(self):
        self.extractor = ImageFeatureExtractor()
        self.creator = ShadowCreator()
        self.exporter = ShadowExporter()
        self.modifier = ShaderModifier()
        self.optimizer = ShadowOptimizer()
        print("QuickShador Library Initialized")

    def run_demo(self):
        print("Running demo...")
        # Example: simulate calling functions
        self.extractor.load_image()
        self.creator.create_drop_shadow()
        self.modifier.increase_opacity()
        self.optimizer.optimize_for_web()
        self.exporter.export_to_png()
