class _Settings(object):
    @apply
    def ALGORITHMS():
        def fget(self):
            a = ['BatAlgorithm', 'HillClimber', 'ParticleSwarmOptimization']
            return a
        return property(**locals())

    @apply
    def BENCHMARKS():
        def fget(self):
            a = ['Griewank', 'Sphere', 'Rosenbrock']
            return a
        return property(**locals())
