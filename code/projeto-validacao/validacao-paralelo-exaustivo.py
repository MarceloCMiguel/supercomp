from grading_utils import PerformanceTest, TestConfiguration, RepeaterTest
import sys

class TestePFEHeuristicoParalelo(ProgramTest, SolucaoValidaMixin, SatisfacaoOtimaMixin):
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Uso: ./validacao-exaustivo executavel')
        sys.exit(-1)

    tests = TestConfiguration.from_pattern('entradas', 'in_exaustivo', check_stderr=False)
    tests['entradas/in_exaustivo_9_3_3'].time_limit = 0.5
    tests['entradas/in_exaustivo_12_4_3'].time_limit = 1.5
    tests['entradas/in_exaustivo_12_4_4'].time_limit = 1.5

    teste_grande = TestConfiguration.from_file('entradas/in_bb_15_5_5',
                                  'entradas/out_bb_15_5_5',
                                  check_stderr=False,
                                  time_limit=60)
    tests['entradas/in_bb_15_5_5'] = teste_grande

    t = PerformanceTest(sys.argv[1], tests)
    t.main()

    teste_repetido = TestConfiguration.from_file('entradas/in_exaustivo_12_4_4', 'entradas/out_exaustivo_12_4_4', check_stderr=False)
    r = RepeaterTest(sys.argv[1], teste_repetido, 10)
    r.main()