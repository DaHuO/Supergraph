#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using value_type = uint32_t;

std::vector<value_type> generate_primes(const value_type max)
{
    std::vector<value_type> primes;
    std::vector<bool> is_prime(max / 2 + 1, true);

    primes.push_back(2);

    for (value_type i = 3; i <= max; i += 2)
    {
        if (is_prime[i / 2])
        {
            primes.push_back(i);
            for (value_type j = i * i; j <= max; j += 2 * i)
            {
                is_prime[j / 2] = false;
            }
        }
    }

    return primes;
}

int main(int argc, char** argv)
{
    if (3 > argc)
    {
        std::cerr << argv[0] << " maximum outfile" << std::endl;
        return 1;
    }

    std::istringstream max_str{argv[1]};
    value_type max;
    max_str >> max;

    auto primes = generate_primes(max);

    std::ofstream out(argv[2], std::ios::binary);
    if (!out.good())
    {
        std::cerr << "Bad output file" << std::endl;
        return 3;
    }

    for (auto p : primes)
    {
        out.write(reinterpret_cast<const char*>(&p), sizeof(value_type));
    }
}
