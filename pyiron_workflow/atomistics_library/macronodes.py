from pyiron_workflow.macro import Macro, macro_node
from pyiron_workflow.atomistics_library.calculatornodes import calc_with_calculator
from pyiron_workflow.atomistics_library.tasknodes import (
    get_elastic_matrix_task_generator,
    get_evcurve_task_generator,
    get_phonons_task_generator,
    analyse_structures,
    generate_structures
)


@macro_node()
def get_energy_volume_curve(wf: Macro) -> None:
    wf.get_task_generator = get_evcurve_task_generator()
    wf.generate_structures = generate_structures(instance=wf.get_task_generator)
    wf.calc_with_calculator = calc_with_calculator(task_dict=wf.generate_structures)
    wf.fit = analyse_structures(instance=wf.get_task_generator, output_dict=wf.calc_with_calculator)
    wf.inputs_map = {
        "get_task_generator__structure": "structure",
        "get_task_generator__num_points": "num_points",
        "get_task_generator__fit_type": "fit_type",
        "get_task_generator__fit_order": "fit_order",
        "get_task_generator__vol_range": "vol_range",
        "get_task_generator__axes": "axes",
        "get_task_generator__strains": "strains",
        "calc_with_calculator__calculator": "calculator",
    }
    wf.outputs_map = {"fit__fit_dict": "fit_dict"}


@macro_node()
def get_elastic_matrix(wf: Macro) -> None:
    wf.get_task_generator = get_elastic_matrix_task_generator()
    wf.generate_structures = generate_structures(instance=wf.get_task_generator)
    wf.calc_with_calculator = calc_with_calculator(task_dict=wf.generate_structures)
    wf.fit = analyse_structures(instance=wf.get_task_generator, output_dict=wf.calc_with_calculator)
    wf.inputs_map = {
        "get_task_generator__structure": "structure",
        "get_task_generator__num_of_point": "num_of_point",
        "get_task_generator__eps_range": "eps_range",
        "get_task_generator__sqrt_eta": "sqrt_eta",
        "get_task_generator__fit_order": "fit_order",
        "calc_with_calculator__calculator": "calculator",
    }
    wf.outputs_map = {"fit__fit_dict": "fit_dict"}


@macro_node()
def get_phonons(wf: Macro) -> None:
    wf.get_task_generator = get_phonons_task_generator()
    wf.generate_structures = generate_structures(instance=wf.get_task_generator)
    wf.calc_with_calculator = calc_with_calculator(task_dict=wf.generate_structures)
    wf.fit = analyse_structures(instance=wf.get_task_generator, output_dict=wf.calc_with_calculator)
    wf.inputs_map = {
        "get_task_generator__structure": "structure",
        "get_task_generator__interaction_range": "interaction_range",
        "get_task_generator__factor": "factor",
        "get_task_generator__displacement": "displacement",
        "get_task_generator__dos_mesh": "dos_mesh",
        "get_task_generator__primitive_matrix": "primitive_matrix",
        "get_task_generator__number_of_snapshots": "number_of_snapshots",
        "calc_with_calculator__calculator": "calculator",
    }
    wf.outputs_map = {"fit__fit_dict": "fit_dict"}
