import importlib.util
import json
from pathlib import Path

import pytest

from tests.test_template import TestTemplate


class TestJapanEconomyNotebook(TestTemplate):
    @pytest.fixture(autouse=True)
    def setup_shared_variables(self, setup):
        self.notebook_path = (
            Path(__file__).resolve().parent.parent / "notebooks" / "japan_economy.py"
        )
        self.nodes_path = (
            Path(__file__).resolve().parent.parent
            / "notebooks"
            / "data"
            / "japan_economy_nodes.json"
        )
        self.treemap_csv_path = (
            Path(__file__).resolve().parent.parent
            / "notebooks"
            / "data"
            / "japan_top50_revenue_treemap_dataset.csv"
        )

    def test_notebook_module_imports(self):
        spec = importlib.util.spec_from_file_location(
            "japan_economy", self.notebook_path
        )
        assert spec is not None
        assert spec.loader is not None

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        assert hasattr(module, "app")

    def test_nodes_cover_expected_sectors_and_companies(self):
        with self.nodes_path.open("r", encoding="utf-8") as nodes_file:
            nodes = json.load(nodes_file)

        labels = {node["label"] for node in nodes}

        assert "Japan economy (2024 nominal GDP)" in labels
        assert "Manufacturing" in labels
        assert "Real estate" in labels
        assert "Wholesale & retail trade" in labels
        assert "Information & communications" in labels
        assert "Toyota" in labels
        assert "NTT" in labels
        assert "Seven & i" in labels

    def test_treemap_csv_contains_public_private_and_mixed_rows(self):
        csv_text = self.treemap_csv_path.read_text(encoding="utf-8")

        assert "Toyota,Public,305.78" in csv_text
        assert "Nippon Life Insurance,Private,72.18" in csv_text
        assert "Rest of covered universe,Mixed,2323.38" in csv_text
