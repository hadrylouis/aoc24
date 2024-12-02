import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.*;

public class part1 {
    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("test.txt"));
        
        List<List<Integer>> columns = IntStream.range(0, 2)
                    .mapToObj(index -> lines.stream()
                            .map(line -> Integer.parseInt(line.split("\\s+")[index]))
                            .collect(Collectors.toList()))
                    .collect(Collectors.toList());

        List<Integer> column1 = columns.get(0).stream().sorted().collect(Collectors.toList());
        List<Integer> column2 = columns.get(1).stream().sorted().collect(Collectors.toList());

        int total = IntStream.range(0, column1.size())
            .map(i -> Math.abs(column1.get(i) - column2.get(i)))
            .sum();

        System.out.println(total);
    }
}