with open("CipherVault/MainWindow.xaml", "r") as f:
    content = f.read()

old_search = """                        <!-- Actions -->
                        <Button Content="Edit" Style="{StaticResource OutlineBtn}" Margin="0,0,8,0" Command="{Binding EditItemCommand}"/>
                        <Button Content="Delete" Style="{StaticResource OutlineBtn}" Foreground="{StaticResource DestructiveBrush}" BorderBrush="{StaticResource DestructiveBrush}" Command="{Binding DeleteItemCommand}"/>
                    </StackPanel>"""

new_search = """                        <!-- Header Utils -->
                        <Button Content="🔄" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="❓" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="👤" Style="{StaticResource ActionBtn}" Margin="0,0,16,0"/>

                        <!-- Actions -->
                        <Button Content="Edit" Style="{StaticResource OutlineBtn}" Margin="0,0,8,0" Command="{Binding EditItemCommand}"/>
                        <Button Content="Delete" Style="{StaticResource OutlineBtn}" Foreground="{StaticResource DestructiveBrush}" BorderBrush="{StaticResource DestructiveBrush}" Command="{Binding DeleteItemCommand}"/>
                    </StackPanel>"""

content = content.replace(old_search, new_search)

with open("CipherVault/MainWindow.xaml", "w") as f:
    f.write(content)
